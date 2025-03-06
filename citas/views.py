from django.shortcuts import render, redirect  # Agregar redirect
from .models import CitaProgramada, Pagaduria, Asesor  # Importar Pagaduria y Asesor

def citas_programadas(request):
    citas = CitaProgramada.objects.all().order_by('fecha', 'hora')
    return render(request, 'citas_programadas.html', {'citas': citas})

def programar_cita(request):
    if request.method == "POST":
        pagaduria_id = request.POST.get("pagaduria")
        asesor_id = request.POST.get("asesor")
        fecha = request.POST.get("fecha")
        hora = request.POST.get("hora")

        CitaProgramada.objects.create(
            pagaduria_id=pagaduria_id,
            asesor_id=asesor_id,
            fecha=fecha,
            hora=hora
        )

        return redirect("programar_citas")  # Asegúrate de que esta URL exista en urls.py

    pagadurias = Pagaduria.objects.all()
    asesores = Asesor.objects.all()  # Corregido "asesor" -> "Asesor"
    return render(request, "programar_citas.html", {"pagadurias": pagadurias, "asesores": asesores})

