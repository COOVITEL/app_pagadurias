from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import datetime, timedelta
from .models import CitaProgramada, Pagaduria
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.urls import reverse

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

def citas_programadas(request):
    citas = CitaProgramada.objects.all().order_by('fecha', 'hora')
    return render(request, 'citas_programadas.html', {'citas': citas})

def programar_cita(request):
    if request.method == "POST":
        pagaduria_nombre = request.POST.get("pagaduria")
        asesor = request.POST.get("asesor")
        fecha = request.POST.get("fecha")
        hora = request.POST.get("hora")

        # Validaciones
        if not all([pagaduria_nombre, asesor, fecha, hora]):
            messages.error(request, "Todos los campos son obligatorios")
            return redirect(reverse('citas:programar_cita'))

        # Validar que la fecha no sea fin de semana
        fecha_dt = datetime.strptime(fecha, '%Y-%m-%d')
        if fecha_dt.weekday() >= 5:  # 5 = Sábado, 6 = Domingo
            messages.error(request, "No se pueden programar citas en fin de semana")
            return redirect(reverse('citas:programar_cita'))

        # Validar que la fecha no sea anterior a hoy
        if fecha_dt.date() < datetime.now().date():
            messages.error(request, "No se pueden programar citas en fechas pasadas")
            return redirect(reverse('citas:programar_cita'))

        # Validar que la hora esté disponible
        hora_str = datetime.strptime(hora, '%H:%M').strftime('%H:%M')
        horas_disponibles = get_horas_disponibles(fecha)
        if hora_str not in horas_disponibles:
            messages.error(request, "La hora seleccionada no está disponible")
            return redirect(reverse('citas:programar_cita'))

        # Crear o obtener la pagaduría
        try:
            pagaduria, created = Pagaduria.objects.get_or_create(
                nombre=pagaduria_nombre
            )
        except Exception as e:
            messages.error(request, f"Error al procesar la pagaduría: {str(e)}")
            return redirect(reverse('citas:programar_cita'))

        # Crear la cita
        try:
            CitaProgramada.objects.create(
                pagaduria=pagaduria,
                asesor=asesor,
                fecha=fecha,
                hora=datetime.strptime(hora, '%H:%M').time(),
                estado='Programada'  # Establecer el estado inicial correcto
            )
            messages.success(request, "Cita programada exitosamente")
            return redirect(reverse('citas:citas_programadas'))
        except ValidationError as e:
            messages.error(request, str(e))
            return redirect(reverse('citas:programar_cita'))
        except Exception as e:
            messages.error(request, f"Error al programar la cita: {str(e)}")
            return redirect(reverse('citas:programar_cita'))

    # GET request
    context = {
        "pagadurias": Pagaduria.objects.all().order_by('nombre'),
        "horas_disponibles": get_horas_disponibles(),
        "min_date": datetime.now().strftime('%Y-%m-%d')
    }
    return render(request, "programar_citas.html", context)

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

def eliminar_cita(request, cita_id):
    if request.method == "POST":
        try:
            cita = get_object_or_404(CitaProgramada, id=cita_id)
            cita.delete()
            messages.success(request, "Cita eliminada exitosamente")
        except Exception as e:
            messages.error(request, f"Error al eliminar la cita: {str(e)}")
    return redirect(reverse('citas:citas_programadas'))
