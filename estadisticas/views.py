from django.shortcuts import render
from .models import Estadistica

def estadisticas(request):
    estadisticas = Estadistica.objects.all()
    return render(request, 'estadisticas/estadisticas.html', {'estadisticas': estadisticas})
