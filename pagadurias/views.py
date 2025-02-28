
from django.shortcuts import render
from .models import Pagaduria  # Asegúrate de importar el modelo correcto

def pagaduriasAprobacion(request):
    pagadurias = Pagaduria.objects.filter(estado='Por aprobar')  # Filtrar por estado si aplica
    return render(request, 'pagaduriasAprobacion.html', {'pagadurias': pagadurias})

def pagadurias(request): # Filtrar por estado si aplica
    return render(request, 'pagadurias.html', {'pagadurias': Pagaduria.objects.filter(estado='Aprobado')})