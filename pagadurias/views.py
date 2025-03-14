
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
        form = PagaduriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pagaduriasAprobacion')
        else:
            print(form.errors)
    else:
        form = PagaduriaForm()
    return render(request, 'createPagaduria.html', {'form': form})

def updatePagaduria(request, id):
    if request.method == "POST":
        pagaduria = Pagaduria.objects.get(pk=id)
        form = PagaduriaForm(request.POST, request.FILES, instance=pagaduria)
        if form.is_valid():
            form.save()
            return redirect('pagaduriasAprobacion')
        else:
            print(form.errors)
    else:
        pagaduria = Pagaduria.objects.get(pk=id)
        form = PagaduriaForm(instance=pagaduria)
    return render(request, 'updatePagaduria.html', {'form': form})