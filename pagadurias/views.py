from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from account.decorators import check_authoritation
from requests.exceptions import ConnectionError
from django.core.paginator import Paginator
from account.models import User
from django.http import FileResponse
from .utils import EmailService, HistorialService
from django.contrib import messages
from django.db.models import Sum
from django.db.models import Q
from .models import HistorialPagaduria, Pagaduria
from .forms import *
import requests

@login_required
@check_authoritation
def pagaduriasAprobacion(request):
    """Listado de las pagadurias pendientes de aprobación"""
    user = request.user
    if user.area == "Asesor":
        pagadurias = Pagaduria.objects.filter(estado="Por aprobar", asesorCreated=user.username)
    else:
        pagadurias = Pagaduria.objects.filter(estado="Por aprobar")
    return render(request, 'pagaduriasAprobacion.html', {'pagadurias': pagadurias})

@login_required
@check_authoritation
def pagadurias(request):
    query = request.GET.get('q', '')
    headers = {
        'Authorization': 'Token aec701eea92de00363e5c40dbdcad62ee7c3eb99'
    }

    # Haces el request al API externo
    datos_pagadurias = []
    try:
        response = requests.get("http://127.0.0.1:8080/api-coovitel/pagadurias", headers=headers)
        if response.status_code == 200:
            datos_pagadurias = response.json()['data']
    except ConnectionError:
        print("Erros al llamar los datos")
    # Indexas los datos externos por NIT para búsqueda rápida
    datos_pagadurias_dict = {item['nit']: item for item in datos_pagadurias}

    # Tus pagadurías locales
    if request.user.area == "Asesor":
        pagadurias_qs = Pagaduria.objects.filter(estadoOperaciones=True, asesores=request.user).order_by("id")
    else:
        pagadurias_qs = Pagaduria.objects.filter(estadoOperaciones=True).order_by("id")

    if query:
        pagadurias_qs = pagadurias_qs.filter(
            Q(nombre__icontains=query) | Q(nit__icontains=query)
        )

    # Ahora, armar una lista de pagadurías locales + su data extra
    pagadurias_list = []
    for pagaduria in pagadurias_qs:
        nit = pagaduria.nit
        data_extra = datos_pagadurias_dict.get(nit, None)  # Busca por NIT
        pagadurias_list.append({
            'pagaduria': pagaduria,
            'data_extra': data_extra,  # puede ser None si no encontró
        })

    paginator = Paginator(pagadurias_list, 10)  # 10 por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pagadurias.html', {
        'pagadurias': page_obj,
        'query': query,
        'paginator': paginator,
        'page_obj': page_obj
    })


@login_required
@check_authoritation
def createPagaduria(request):
    """Crear una nueva pagaduría"""
    if request.method == "POST":
        form = PagaduriaForm(request.POST, request.FILES)
        sucursales = SucursalFormSet(request.POST)

        if form.is_valid() and sucursales.is_valid():
            # Guardar la pagaduría sin commit
            pagaduria_instance = form.save(commit=False)
            pagaduria_instance.asesorCreated = request.user.username
            pagaduria_instance.asesorAsignado = request.user.username
            pagaduria_instance.save()
            
            HistorialService.registrar_historial(
                pagaduria=pagaduria_instance,
                accion='Creación',
                realizado_por=request.user,
                descripcion='Se creó la pagaduría.'
            )

            # Asignar asesor actual
            user = request.user
            pagaduria_instance.asesores.add(user)

            # Obtener correos del asesor actual y usuarios del grupo Comercial
            correos_comercial = User.objects.filter(
                groups__name='Comercial'
            ).values_list('email', flat=True)

            # Lista de destinatarios (sin duplicados)
            destinatarios = list(set([user.email] + list(correos_comercial)))

            # Enviar correo
            EmailService.enviar_creacion_pagaduria(pagaduria_instance, destinatarios)

            # Guardar las sucursales asociadas
            for sucursal in sucursales:
                if sucursal.is_valid() and not sucursal.cleaned_data.get('DELETE'):
                    sucursal_instance = sucursal.save(commit=False)
                    sucursal_instance.pagaduria = pagaduria_instance
                    sucursal_instance.save()
                else:
                    print(f"Error en sucursal {sucursal.prefix}: {sucursal.errors}")

            messages.success(request, "✅ La pagaduría se ha creado exitosamente.")
            return redirect('pagaduriasAprobacion')
        else:
            messages.error(request, "❌ Hubo errores al crear la pagaduría. Por favor, revisa los campos.")
            print("error")
            print(form.errors)
            print(sucursales.errors)
    else:
        form = PagaduriaForm()
        sucursales = SucursalFormSet()

    return render(request, 'createPagaduria.html', {
        'form': form,
        'sucursales': sucursales,
    })


@login_required
@check_authoritation
def updatePagaduria(request, id, token):
    """ Actualizar información de las pagadurías. """
    if request.method == "POST":
        pagaduria = Pagaduria.objects.get(id=id, tokenControl=token)
        form = PagaduriaUpdateDatasForm(request.POST, request.FILES, instance=pagaduria)
        sucursalesForm = SucursalFormSet(request.POST, prefix='sucursales', instance=pagaduria)

        if form.is_valid() and sucursalesForm.is_valid():
            # Guardar la pagaduría primero
            pagaduria_instance = form.save(commit=False)
            pagaduria_instance.asesorCreated = request.user.username
            pagaduria_instance.asesorAsignado = request.user.username
            pagaduria_instance.save()
            
            HistorialService.registrar_historial(
                pagaduria=pagaduria_instance,
                accion='Actualización',
                realizado_por=request.user,
                descripcion='Se actualizó la información de la pagaduría.'
            )
            
            # Definir los destinatarios (por ejemplo, los asesores de la pagaduría)
            destinatarios = [usuario.email for usuario in pagaduria_instance.asesores.all()]

            # Llamar al servicio de notificación para enviar el correo
            EmailService.enviar_actualizacion_pagaduria(pagaduria_instance, destinatarios)


            # Guardar las sucursales asociadas
            sucursalesForm.save()  # Esto maneja tanto las instancias existentes como las nuevas
            asesores_ids = request.POST.getlist('asesores')
            pagaduria.asesores.set(asesores_ids)

            messages.success(request, "✅ La pagaduría se ha actualizado exitosamente.")
            return redirect('updatePagaduria', id=id, token=token)
        else:
            messages.error(request, "❌ Hubo errores al actualizar la pagaduría. Por favor, revisa los campos.")
            print("error")
            print(form.errors)
            print(sucursalesForm.errors)
    else:
        pagaduria = Pagaduria.objects.get(id=id, tokenControl=token)
        form = PagaduriaUpdateDatasForm(instance=pagaduria)
        sucursalesForm = SucursalFormSet(instance=pagaduria, prefix='sucursales')
        asesores = User.objects.all()  # ✅ MOSTRAR TODOS LOS USUARIOS
        asesores_seleccionados = pagaduria.asesores.values_list('id', flat=True)
            
            
            
    historial = HistorialService.obtener_historial(pagaduria)
            
    return render(request, 'updatePagaduria.html', {
        'form': form,
        'pagaduria': pagaduria,
        'sucursalesForm': sucursalesForm,
        'asesores': asesores,
        'asesores_seleccionados': asesores_seleccionados,
        'historial': historial,
        })

@login_required
@check_authoritation
def info_pagaduria(request, pagaduria_id):
    pagaduria = get_object_or_404(Pagaduria, id=pagaduria_id)
    sucursales = pagaduria.sucursales.all()

    # Calcular totales
    totales = sucursales.aggregate(
        totalEmpleados=Sum('totalEmpleados'),
        indefinidos=Sum('empleadosIndefinidos'),
        fijos=Sum('empleadosFijo'),
        obra=Sum('empleadosObraLabor'),
        otros=Sum('empleadosOtros'),
        salario1y2=Sum('empleadosSalario1y2'),
        salario2y4=Sum('empleadosSalario2y4'),
        salarioMax4=Sum('empleadosSalariomax4')
    )

    return render(request, 'infoPagaduria.html', {
        'pagaduria': pagaduria,
        'sucursales': sucursales,
        'totales': totales
    })

@login_required
@check_authoritation
def descargar_archivo(request, pagaduria_id, field_name):
    pagaduria = get_object_or_404(Pagaduria, id=pagaduria_id)
    file_field = getattr(pagaduria, field_name)
    response = FileResponse(file_field)
    return response

@login_required
@check_authoritation
def check_comercial(request, name, token):
    pagaduria = get_object_or_404(Pagaduria, nombre=name, tokenControl=token)
    if request.method == "POST":
        form = PagaduriaUpdateComercialForm(request.POST, instance=pagaduria)
        formObservacion = ObservacionPagaduriaForm(request.POST)
        if form.is_valid() and formObservacion.is_valid():
            form.save()
            
            HistorialService.registrar_historial(
                pagaduria=pagaduria,
                accion='Aprobación Comercial',
                realizado_por=request.user,
                descripcion='La pagaduría fue aprobada por el área Comercial.'
            )
            
            observacion = formObservacion.save(commit=False)
            observacion.pagaduria = pagaduria
            observacion.creadoPor = request.user
            observacion.area = request.user.area
            observacion.save()

            messages.success(request, "✅ ¡Se ha aprobado la pagaduría con éxito!")

            # Obtener correos del grupo "Financiero"
            correos_financiero = User.objects.filter(area="Financiero", is_active=True).values_list('email', flat=True)

            # Enviar notificación de cambio de estado a "Financiero"
            EmailService.enviar_cambio_estado(pagaduria, correos_financiero)

            return redirect('pagaduriasAprobacion')
    else:
        form = PagaduriaUpdateComercialForm()
        formObservacion = ObservacionPagaduriaForm()
        
    return render(request, 'aprobacion/aprobacion_comercial.html', {
        'form': form,
        'pagaduria': pagaduria,
        'formObservacion': formObservacion
    })


@login_required
@check_authoritation
def check_financiero(request, name, token):
    pagaduria = get_object_or_404(Pagaduria, nombre=name, tokenControl=token)
    observacionesPrevias = ObservacionesPagaduria.objects.filter(pagaduria=pagaduria, area="Financiero")
    
    if request.method == "POST":
        form = PagaduriaUpdateFinancieraForm(request.POST, instance=pagaduria)
        formObservacion = ObservacionPagaduriaForm(request.POST)
        
        if form.is_valid() and formObservacion.is_valid():
            form.save()
            HistorialService.registrar_historial(
                pagaduria=pagaduria,
                accion='Aprobación Financiero',
                realizado_por=request.user,
                descripcion='La pagaduría fue aprobada por el área Comercial.'
            )

            observacion = formObservacion.save(commit=False)
            observacion.pagaduria = pagaduria
            observacion.creadoPor = request.user
            observacion.area = request.user.area
            observacion.save()

            # Obtener correos del área "Riesgos"
            correos_riesgos = User.objects.filter(area="Riesgos", is_active=True).values_list('email', flat=True)

            # Enviar notificación de cambio de estado a usuarios de Riesgos
            EmailService.enviar_cambio_estado(pagaduria, correos_riesgos)

            messages.success(request, "✅ La pagaduría fue aprobada por el área financiera.")
            return redirect('pagaduriasAprobacion')
    
    else:
        form = PagaduriaUpdateFinancieraForm()
        formObservacion = ObservacionPagaduriaForm()

    return render(request, 'aprobacion/aprobacion_financiera.html', {
        'observacionesPrevias': observacionesPrevias,
        'form': form,
        'pagaduria': pagaduria,
        'formObservacion': formObservacion
    })


@login_required
@check_authoritation
def check_riesgos(request, name, token):
    pagaduria = get_object_or_404(Pagaduria, nombre=name, tokenControl=token)

    if request.method == "POST":
        form = PagaduriaUpdateRiesgosForm(request.POST, instance=pagaduria)
        formObservacion = ObservacionPagaduriaForm(request.POST)

        if form.is_valid() and formObservacion.is_valid():
            form.save()
            HistorialService.registrar_historial(
                pagaduria=pagaduria,
                accion='Aprobación Riesgos',
                realizado_por=request.user,
                descripcion='La pagaduría fue aprobada por el área Comercial.'
            )

            observacion = formObservacion.save(commit=False)
            observacion.pagaduria = pagaduria
            observacion.creadoPor = request.user
            observacion.area = request.user.area
            observacion.save()

            # Notificar a usuarios de operaciones
            correos_operaciones = User.objects.filter(area="Operaciones", is_active=True).values_list('email', flat=True)
            EmailService.enviar_cambio_estado(pagaduria, correos_operaciones)

            messages.success(request, "✅ La pagaduría fue aprobada por el área de riesgos.")
            return redirect('pagaduriasAprobacion')

    else:
        form = PagaduriaUpdateRiesgosForm()
        formObservacion = ObservacionPagaduriaForm()

    return render(request, 'aprobacion/aprobacion_riesgos.html', {
        'form': form,
        'pagaduria': pagaduria,
        'formObservacion': formObservacion
    })

    
@login_required
@check_authoritation
def lista_operaciones(request):
    pagadurias = Pagaduria.objects.filter(
        estadoComercial="Aprobado",
        estadoFinanciero="Aprobado",
        estadoRiesgos="Aprobado",
        estadoOperaciones=False
    )
    return render(request, 'operaciones/lista_operaciones.html', {
        'pagadurias': pagadurias
    })

@login_required
@check_authoritation
def aprobar_operaciones(request, name, token):
    pagaduria = get_object_or_404(Pagaduria, nombre=name, tokenControl=token)

    if request.method == "POST":
        pagaduria.estadoOperaciones = True
        pagaduria.save()
        
        HistorialService.registrar_historial(
            pagaduria=pagaduria,
            accion='Aprobación Operaciones',
            realizado_por=request.user,
            descripcion='La pagaduría fue aprobada por el área de Operaciones.'
        )
        
        # Obtener el usuario asesor asignado a partir del username
        asesor_username = pagaduria.asesorAsignado
        asesor = User.objects.filter(username=asesor_username, is_active=True).first()

        # Validar si el asesor existe y tiene correo
        if asesor and asesor.email:
            destinatarios = [asesor.email]
            EmailService.enviar_cambio_estado(pagaduria, destinatarios)

        messages.success(request, "¡Pagaduría aprobada en Operaciones!")
        return redirect('pagadurias')

    return render(request, 'operaciones/aprobar_operaciones.html', {
        'pagaduria': pagaduria
    })


@login_required
@check_authoritation
def check_rechazo(request, name, token):
    pagaduria = get_object_or_404(Pagaduria, nombre=name, tokenControl=token)

    # Determinar el área de rechazo
    area = ""
    rechazo = ""
    if pagaduria.estadoComercial == "Rechazado por Politicas" or pagaduria.estadoComercial == "Rechazado por Documentación":
        area = "Comercial"
        rechazo = pagaduria.estadoComercial
    elif pagaduria.estadoFinanciero == "Rechazado por Politicas" or pagaduria.estadoFinanciero == "Rechazado por Documentación":
        area = "Financiero"
        rechazo = pagaduria.estadoFinanciero
    elif pagaduria.estadoRiesgos == "Rechazado por Politicas" or pagaduria.estadoRiesgos == "Rechazado por Documentación":
        area = "Riesgos"
        rechazo = pagaduria.estadoRiesgos

    # Manejo de formulario POST
    if request.method == "POST":        
        formObservacion = ObservacionPagaduriaForm(request.POST)
        if formObservacion.is_valid():
            observacion = formObservacion.save(commit=False)
            observacion.pagaduria = pagaduria
            observacion.area = "Asesor"
            observacion.creadoPor = request.user
            observacion.save()
            
            HistorialService.registrar_historial(
                pagaduria=pagaduria,
                accion='Revisión tras rechazo',
                realizado_por=request.user,
                descripcion='Se agregó una observación y se reinició el estado del área correspondiente.'
            )
    
            # Cambiar estado a "Pendiente" en el área correspondiente
            if pagaduria.estadoComercial == "Rechazado por Politicas" or pagaduria.estadoComercial == "Rechazado por Documentación":
                pagaduria.estadoComercial = "Pendiente"
            elif pagaduria.estadoFinanciero == "Rechazado por Politicas" or pagaduria.estadoFinanciero == "Rechazado por Documentación":
                pagaduria.estadoFinanciero = "Pendiente"
            elif pagaduria.estadoRiesgos == "Rechazado por Politicas" or pagaduria.estadoRiesgos == "Rechazado por Documentación":
                pagaduria.estadoRiesgos = "Pendiente"
            pagaduria.save()
            
            # Enviar notificación a los usuarios del área correspondiente
            #destinatarios = [usuario.email for usuario in User.objects.filter(area=area, is_active=True)]
            
            #EmailService.enviar_cambio_estado(pagaduria, destinatarios)
            
            return redirect('pagaduriasAprobacion')
    else:
        formObservacion = ObservacionPagaduriaForm()
        observaciones = ObservacionesPagaduria.objects.filter(area=area, pagaduria=pagaduria)
        form = PagaduriaUpdateDocumentsForm(instance=pagaduria)
    return render(request, 'checkRechazo.html', {
        'pagaduria': pagaduria,
        'observaciones': observaciones,
        'area': area,
        'rechazo': rechazo,
        'formObservacion': formObservacion,
        'form': form
    })

@login_required
@check_authoritation
def historial_pagaduria_view(request, pagaduria_id):
    pagaduria = get_object_or_404(Pagaduria, id=pagaduria_id)
    historial = HistorialPagaduria.objects.filter(pagaduria=pagaduria).order_by('-fecha')
    return render(request, 'pagaduria/infoPagaduria.html', {
        'pagaduria': pagaduria,
        'historial': historial
    })