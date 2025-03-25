from django.shortcuts import render, redirect, get_object_or_404
from .models import Pagaduria
from .forms import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import FileResponse
from account.decorators import check_authoritation
import uuid

@login_required
@check_authoritation
def pagaduriasAprobacion(request):
    """Listado de las pagadurias pendientes de aprobación"""
    pagadurias = Pagaduria.objects.filter(estado="Por aprobar")
    return render(request, 'pagaduriasAprobacion.html', {'pagadurias': pagadurias})

@login_required
@check_authoritation
def pagadurias(request):
    """Listado de las pagadurias aprobadas y activas en linix"""
    pagadurias = Pagaduria.objects.filter(estado='Aprobado')
    return render(request, 'pagadurias.html', {'pagadurias': pagadurias})

@login_required
@check_authoritation
def createPagaduria(request):
    """Crear una nueva pagaduria"""
    if request.method == "POST":
        form = PagaduriaForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.asesorCreated = request.user.username
            instance.asesorAsignado = request.user.username
            instance.save()
            return redirect('pagaduriasAprobacion')
        else:
            print(form.errors)
    else:
        form = PagaduriaForm()
    return render(request, 'createPagaduria.html', {'form': form})

@login_required
@check_authoritation
def updatePagaduria(request, id):
    """ Actualizar informacion de las pagadurias. """
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
@check_authoritation
def info_pagaduria(request, pagaduria_id):
    """ Visualizacion de la informacion de la pagaduria """
    pagaduria = get_object_or_404(Pagaduria, id=pagaduria_id)
    # if is_financiero(request.user):
    #     user_role = 'Financiero'
    # elif is_comercial(request.user):
    #     user_role = 'Comercial'
    # elif is_riesgos(request.user):
    #     user_role = 'Riesgos'
    # else:
    #     user_role = 'None'
    # return render(request, 'infoPagaduria.html', {'pagaduria': pagaduria, 'user_role': user_role})
    return render(request, 'infoPagaduria.html', {'pagaduria': pagaduria})

@login_required
@check_authoritation
def descargar_archivo(request, pagaduria_id, field_name):
    pagaduria = get_object_or_404(Pagaduria, id=pagaduria_id)
    file_field = getattr(pagaduria, field_name)
    response = FileResponse(file_field)
    return response

@login_required
@check_authoritation
def check_financiero(request, name, token):
    pagaduria = get_object_or_404(Pagaduria, nombre=name, tokenControl=token)
    if request.method == "POST":
        form = PagaduriaUpdateFinancieraForm(request.POST, instance=pagaduria)
        if form.is_valid():
            form.save()
            return redirect('pagaduriasAprobacion')
    else:
        form = PagaduriaUpdateFinancieraForm()
    return render(request, 'aprobacion_financiera.html', {'form': form, 'pagaduria': pagaduria})

@login_required
@check_authoritation
def check_riesgos(request, name, token):
    pagaduria = get_object_or_404(Pagaduria, nombre=name, tokenControl=token)
    if request.method == "POST":
        form = PagaduriaUpdateRiesgosForm(request.POST, instance=pagaduria)
        if form.is_valid():
            form.save()
            return redirect('pagaduriasAprobacion')
    else:
        form = PagaduriaUpdateRiesgosForm()
    return render(request, 'aprobacion_riesgos.html', {'form': form, 'pagaduria': pagaduria})

@login_required
@check_authoritation
def check_comercial(request, name, token):
    pagaduria = get_object_or_404(Pagaduria, nombre=name, tokenControl=token)
    if request.method == "POST":
        form = PagaduriaUpdateComercialForm(request.POST, instance=pagaduria)
        if form.is_valid():
            instan = form.save(commit=False)
            if instan.estadoComercial == 'Aprobado':
                instan.estado = 'Aprobado'
            form.save()
            return redirect('pagaduriasAprobacion')
    else:
        form = PagaduriaUpdateComercialForm()
    return render(request, 'aprobacion_comercial.html', {'form': form, 'pagaduria': pagaduria})


def is_financiero(user):
    return user.groups.filter(name='Financiero').exists()

def is_comercial(user):
    return user.groups.filter(name='Comercial').exists()

def is_riesgos(user):
    return user.groups.filter(name='Riesgos').exists()

