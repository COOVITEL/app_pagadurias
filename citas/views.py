from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from account.decorators import check_authoritation, check_for_pagadurias
from django.contrib import messages
from datetime import datetime, timedelta
from .models import CitaProgramada
from django.core.exceptions import ValidationError
from pagadurias.models import Pagaduria
from django.http import JsonResponse
from django.urls import reverse
from .forms import CitaProgramadaForm, CitaProgramadaCloseForm
from datetime import date

@login_required
@check_authoritation
def get_horas_disponibles(fecha=None, exclude_cita_id=None):

    # Horario de atención: 8:00 AM a 5:00 PM
    horas_base = [
        '08:00', '09:00', '10:00', '11:00', '12:00',
        '14:00', '15:00', '16:00', '17:00'
    ]
    
    if not fecha:
        return horas_base
        
    # Si se proporciona una fecha, filtrar las horas ya reservadas
    citas_del_dia = CitaProgramada.objects.filter(fecha=fecha)
    if exclude_cita_id:
        citas_del_dia = citas_del_dia.exclude(id=exclude_cita_id)
    horas_ocupadas = [cita.hora.strftime('%H:%M') for cita in citas_del_dia]
    
    return [hora for hora in horas_base if hora not in horas_ocupadas]

@login_required
@check_authoritation
def citas_programadas(request):
    today = date.today() - timedelta(days=1)
    citas = CitaProgramada.objects.filter(fecha__gt=today).exclude(estado="Completada").order_by('fecha', 'hora')
    cita = None
    find = None
    citaEncontrada = None
    if request.method == "POST":
            form_type = request.POST.get('form-type')
            if form_type == 'open-cita':
                citaId = request.POST.get('cita-id')
                cita = CitaProgramada.objects.get(id=citaId)
                find = True
                citaEncontrada = CitaProgramadaCloseForm(instance=cita)
            
            elif form_type == "update-cita":
                citaId = request.POST.get('cita-id')
                cita = CitaProgramada.objects.get(id=citaId)
                citaEncontrada = CitaProgramadaCloseForm(request.POST, instance=cita)
                if citaEncontrada.is_valid():
                    cita.estado = 'Completada'
                    citaEncontrada.save()
                    cita.save()
                    messages.success(request, "Se ha finalizado la cita con exito exito")
                    return redirect('citas_programadas')
                find = True
    
    return render(request, 'citas_programadas.html', {
        'citas': citas,
        'find': find,
        'citaFind': cita,
        'citaEncontrada': citaEncontrada
        })

@login_required
@check_authoritation
def programar_cita(request):
    print(request.user.area)
    if request.method == "POST":
        form = CitaProgramadaForm(request.POST, user=request.user)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Cita programada correctamente.")
                return redirect('citas_programadas')
            except ValidationError as e:
                # Añadir los errores al formulario
                form.add_error(None, e)
                messages.error(request, f"Error al guardar la cita: {e}")
        else:
            messages.error(request, f"Formulario inválido: {form.errors.as_text()}")
            return redirect('programar_cita')
        
        # En caso de error, renderiza con los mensajes y el formulario
        return render(request, "programar_citas.html", {'form': form})
    
    else:
        form = CitaProgramadaForm(user=request.user)
    return render(request, "programar_citas.html", {'form': form})


@login_required
@check_authoritation
def editar_cita(request, cita_id):

    cita = get_object_or_404(CitaProgramada, id=cita_id)
    
    if request.method == "POST":
        pagaduria_nombre = request.POST.get("pagaduria")
        asesor = request.POST.get("asesor")
        fecha = request.POST.get("fecha")
        hora = request.POST.get("hora")
        estado = request.POST.get("estado")
        notas = request.POST.get("notas")

        # Validaciones
        if not all([pagaduria_nombre, asesor, fecha, hora]):
            messages.error(request, "Todos los campos son obligatorios")
            return redirect(reverse('citas:editar_cita', args=[cita_id]))

        # Validar que la fecha no sea fin de semana
        fecha_dt = datetime.strptime(fecha, '%Y-%m-%d')
        if fecha_dt.weekday() >= 5:  # 5 = Sábado, 6 = Domingo
            messages.error(request, "No se pueden programar citas en fin de semana")
            return redirect(reverse('citas:editar_cita', args=[cita_id]))

        # Validar que la hora esté disponible (excluyendo la cita actual)
        hora_str = datetime.strptime(hora, '%H:%M').strftime('%H:%M')
        horas_disponibles = get_horas_disponibles(fecha, exclude_cita_id=cita_id)
        if hora_str not in horas_disponibles:
            messages.error(request, "La hora seleccionada no está disponible")
            return redirect(reverse('citas:editar_cita', args=[cita_id]))

        try:
            # Actualizar o crear la pagaduría
            pagaduria, created = Pagaduria.objects.get_or_create(
                nombre=pagaduria_nombre
            )
            
            # Actualizar la cita
            cita.pagaduria = pagaduria
            cita.asesor = asesor
            cita.fecha = fecha
            cita.hora = datetime.strptime(hora, '%H:%M').time()
            if estado:
                cita.estado = estado
            if notas:
                cita.notas = notas
            cita.save()
            
            messages.success(request, "Cita actualizada exitosamente")
            return redirect(reverse('citas:citas_programadas'))
        except ValidationError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, f"Error al actualizar la cita: {str(e)}")
        
        return redirect(reverse('citas:editar_cita', args=[cita_id]))

    # GET request
    context = {
        "cita": cita,
        "pagadurias": Pagaduria.objects.all().order_by('nombre'),
        "horas_disponibles": get_horas_disponibles(cita.fecha, exclude_cita_id=cita.id),
        "min_date": datetime.now().strftime('%Y-%m-%d')
    }
    return render(request, "editar_cita.html", context)

@login_required
@check_authoritation
def cancelar_cita(request, cita_id):
    
    if request.method == "POST":
        try:
            cita = get_object_or_404(CitaProgramada, id=cita_id)
            cita.estado = "Cancelada"
            cita.save()
            messages.success(request, "Cita cancelada exitosamente")
        except Exception as e:
            messages.error(request, f"Error al eliminar la cita: {str(e)}")
    return redirect('citas_programadas')

@login_required
@check_authoritation
@check_for_pagadurias
def start_cita(request, cita_id):
    if request.method == 'POST':
        try:
            cita = get_object_or_404(CitaProgramada, id=cita_id)
            cita.estado = "En atención"
            cita.save()
            messages.success(request, "Se inicio la atencion de la cita, recuerde cerrarla al finalizar")
        except Exception as e:
            messages.error(request, "A ocurrido un error al iniciar la antencion, intentalo de nuevo")
    return redirect('citas_programadas')
