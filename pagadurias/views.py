
from django.shortcuts import render, redirect
from .models import Pagaduria
from .forms import PagaduriaForm

def pagaduriasAprobacion(request):
    pagadurias = Pagaduria.objects.filter(estado='Por aprobar')  # Filtrar por estado si aplica
    return render(request, 'pagaduriasAprobacion.html', {'pagadurias': pagadurias})

def pagadurias(request): # Filtrar por estado si aplica
    return render(request, 'pagadurias.html', {'pagadurias': Pagaduria.objects.filter(estado='Aprobado')})

def createPagaduria(request):
    if request.method == "POST":
        form = PagaduriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagaduriasAprobacion')
    else:
        form = PagaduriaForm()
    return render(request, 'createPagaduria.html', {'form': form})