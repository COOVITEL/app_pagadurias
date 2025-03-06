from django.shortcuts import render
from .models import Operacion

def lista_operaciones(request):
    operaciones = Operacion.objects.all()
    return render(request, 'operaciones/lista_operaciones.html', {'operaciones': operaciones})
