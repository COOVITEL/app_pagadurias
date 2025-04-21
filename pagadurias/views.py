from django.shortcuts import render, redirect, get_object_or_404
from .models import Pagaduria
from .forms import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import FileResponse
from account.decorators import check_authoritation
from .utils import getDepartamentAndCitys
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages

@login_required
@check_authoritation
def pagaduriasAprobacion(request):
    """Listado de las pagadurias pendientes de aprobación"""
    pagadurias = Pagaduria.objects.filter(estado="Por aprobar")
    for pagaduria in pagadurias:
        pagaduria.checkRechazoFinanciera = pagaduria.checkRechazoFinanciero(request.user)
    return render(request, 'pagaduriasAprobacion.html', {'pagadurias': pagadurias})

@login_required
@check_authoritation
def pagadurias(request):
    query = request.GET.get('q', '')

    pagadurias = Pagaduria.objects.filter(estado='Aprobado')
    if query:
        pagadurias = pagadurias.filter(
            Q(nombre__icontains=query) | Q(nit__icontains=query)
        )

    paginator = Paginator(pagadurias, 10)  # 10 por página
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
            # Guardar la pagaduría primero
            pagaduria_instance = form.save(commit=False)
            pagaduria_instance.asesorCreated = request.user.username
            pagaduria_instance.asesorAsignado = request.user.username
            pagaduria_instance.save()

            # Guardar las sucursales asociadas
            for sucursal in sucursales:
                if sucursal.is_valid() and not sucursal.cleaned_data.get('DELETE'):
                    sucursal_instance = sucursal.save(commit=False)
                    sucursal_instance.pagaduria = pagaduria_instance
                    sucursal_instance.save()
                else:
                    # messages.error(request, f"Error en sucursal {sucursal.prefix}: {sucursal.errors}")
                    print(f"Error en sucursal {sucursal.prefix}: {sucursal.errors}")

            messages.success(request, "✅ La pagaduría se ha creado exitosamente.")
            return redirect('pagaduriasAprobacion')
        else:
            
            messages.error(request, "❌ Hubo errores al crear la pagaduría. Por favor, revisa los campos.")
            print("error")
            print(form.errors)
            print(sucursales.errors)
            # messages.error(request, "Error en el formulario de pagaduría")

    else:
        
        form = PagaduriaForm()
        sucursales = SucursalFormSet()

    return render(request, 'createPagaduria.html', 
                {
                    'form': form,
                    'sucursales': sucursales,
                })

@login_required
@check_authoritation
def updatePagaduria(request, nombre, token):
    """ Actualizar informacion de las pagadurias. """
    if request.method == "POST":
        pagaduria = Pagaduria.objects.get(nombre=nombre, tokenControl=token)
        form = PagaduriaUpdateDatasForm(request.POST, request.FILES, instance=pagaduria)
        sucursalesForm = SucursalFormSet(request.POST, prefix='sucursales')
        if form.is_valid():
            form.save()
            return redirect('pagaduriasAprobacion')
        else:
            print(form.errors)
    else:
        pagaduria = Pagaduria.objects.get(nombre=nombre, tokenControl=token)
        form = PagaduriaUpdateDatasForm(instance=pagaduria)
        sucursalesForm = SucursalFormSet(instance=pagaduria, prefix='sucursales')
    return render(request, 'updatePagaduria.html', {'form': form, 'pagaduria': pagaduria, 'sucursalesForm': sucursalesForm})

@login_required
@check_authoritation
def info_pagaduria(request, pagaduria_id):
    """ Visualizacion de la informacion de la pagaduria """
    pagaduria = get_object_or_404(Pagaduria, id=pagaduria_id)
    # if is_financiero(request.user):
    #     user_role = 'Financiero'
    # elif is_comercial(request.user):
    #     user_role = 'Comercial'
    # elif is_riesgos(request.user):
    #     user_role = 'Riesgos'
    # else:
    #     user_role = 'None'
    # return render(request, 'infoPagaduria.html', {'pagaduria': pagaduria, 'user_role': user_role})
    return render(request, 'infoPagaduria.html', {'pagaduria': pagaduria})

@login_required
@check_authoritation
def descargar_archivo(request, pagaduria_id, field_name):
    pagaduria = get_object_or_404(Pagaduria, id=pagaduria_id)
    file_field = getattr(pagaduria, field_name)
    response = FileResponse(file_field)
    return response

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
            observacion = formObservacion.save(commit=False)
            observacion.pagaduria = pagaduria
            observacion.creadoPor = request.user
            observacion.area = request.user.area
            observacion.save()
            return redirect('pagaduriasAprobacion')
        # Cambio 
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
            observacion = formObservacion.save(commit=False)
            observacion.pagaduria = pagaduria
            observacion.creadoPor = request.user
            observacion.area = request.user.area
            observacion.save()
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
def check_comercial(request, name, token):
    pagaduria = get_object_or_404(Pagaduria, nombre=name, tokenControl=token)
    if request.method == "POST":
        form = PagaduriaUpdateComercialForm(request.POST, instance=pagaduria)
        formObservacion = ObservacionPagaduriaForm(request.POST)
        if form.is_valid() and formObservacion.is_valid():
            form.save()
            observacion = formObservacion.save(commit=False)
            observacion.pagaduria = pagaduria
            observacion.creadoPor = request.user
            observacion.area = request.user.area
            observacion.save()
            return redirect('pagaduriasAprobacion')
    else:
        form = PagaduriaUpdateComercialForm()
        formObservacion = ObservacionPagaduriaForm()
        
    return render(request, 'aprobacion/aprobacion_comercial.html', {
        'form': form,
        'pagaduria': pagaduria,
        'formObservacion': formObservacion
        })

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

            # Cambiar estado a "Pendiente" en el área correspondiente
            if pagaduria.estadoComercial == "Rechazado por Politicas" or pagaduria.estadoComercial == "Rechazado por Documentación":
                pagaduria.estadoComercial = "Pendiente"
            elif pagaduria.estadoFinanciero == "Rechazado por Politicas" or pagaduria.estadoFinanciero == "Rechazado por Documentación":
                pagaduria.estadoFinanciero = "Pendiente"
            elif pagaduria.estadoRiesgos == "Rechazado por Politicas" or pagaduria.estadoRiesgos == "Rechazado por Documentación":
                pagaduria.estadoRiesgos = "Pendiente"
            pagaduria.save()
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


def is_financiero(user):
    return user.groups.filter(name='Financiero').exists()

def is_comercial(user):
    return user.groups.filter(name='Comercial').exists()

def is_riesgos(user):
    return user.groups.filter(name='Riesgos').exists()
