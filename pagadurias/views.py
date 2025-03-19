from django.shortcuts import render, redirect, get_object_or_404
from .models import Pagaduria
from .forms import PagaduriaForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import FileResponse

def is_financiero(user):
    return user.groups.filter(name='Financiero').exists()

def is_comercial(user):
    return user.groups.filter(name='Comercial').exists()

def is_riesgos(user):
    return user.groups.filter(name='Riesgos').exists()

@login_required
@user_passes_test(is_financiero)
def aprobar_financiero(request, pagaduria_id):
    pagaduria = get_object_or_404(Pagaduria, id=pagaduria_id)
    pagaduria.estado_financiero = 'Aprobado'
    pagaduria.save()
    return redirect('pagaduriasAprobacion')

@login_required
@user_passes_test(is_comercial)
def aprobar_comercial(request, pagaduria_id):
    pagaduria = get_object_or_404(Pagaduria, id=pagaduria_id)
    if pagaduria.estado_financiero == 'Aprobado':
        pagaduria.estado_comercial = 'Aprobado'
        pagaduria.save()
    return redirect('pagaduriasAprobacion')

@login_required
@user_passes_test(is_riesgos)
def aprobar_riesgos(request, pagaduria_id):
    pagaduria = get_object_or_404(Pagaduria, id=pagaduria_id)
    if pagaduria.estado_financiero == 'Aprobado' and pagaduria.estado_comercial == 'Aprobado':
        pagaduria.estado_riesgos = 'Aprobado'
        pagaduria.save()
    return redirect('pagaduriasAprobacion')

@login_required
def pagaduriasAprobacion(request):
    pagadurias = Pagaduria.objects.all()
    if is_financiero(request.user):
        user_role = 'Financiero'
    elif is_comercial(request.user):
        user_role = 'Comercial'
    elif is_riesgos(request.user):
        user_role = 'Riesgos'
    else:
        user_role = 'None'
    return render(request, 'pagaduriasAprobacion.html', {'pagadurias': pagadurias, 'user_role': user_role})

@login_required
def pagadurias(request):
    pagadurias = Pagaduria.objects.filter(estado='Aprobado')
    return render(request, 'pagadurias.html', {'pagadurias': pagadurias})

@login_required
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

@login_required
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

@login_required
def info_pagaduria(request, pagaduria_id):
    pagaduria = get_object_or_404(Pagaduria, id=pagaduria_id)
    if is_financiero(request.user):
        user_role = 'Financiero'
    elif is_comercial(request.user):
        user_role = 'Comercial'
    elif is_riesgos(request.user):
        user_role = 'Riesgos'
    else:
        user_role = 'None'
    return render(request, 'infoPagaduria.html', {'pagaduria': pagaduria, 'user_role': user_role})

@login_required
def descargar_archivo(request, pagaduria_id, field_name):
    pagaduria = get_object_or_404(Pagaduria, id=pagaduria_id)
    file_field = getattr(pagaduria, field_name)
    response = FileResponse(file_field)
    return response