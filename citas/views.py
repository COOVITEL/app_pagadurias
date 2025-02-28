from django.shortcuts import render
from .models import CitaProgramada

def citas_programadas(request):
    citas = CitaProgramada.objects.all().order_by('fecha', 'hora')  # Ordenar por fecha y hora
    return render(request, 'citas_programadas.html', {'citas': citas})
