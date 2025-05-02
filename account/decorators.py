from functools import wraps
from django.shortcuts import redirect

def check_authoritation(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.checkForTI or request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        return redirect('waiting_for_auth')
    return _wrapped_view

def check_superuser(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        return redirect('administrador')
    return _wrapped_view

def check_operaciones(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.area in ['Director', 'TI', 'Operaciones']:
            return view_func(request, *args, **kwargs)
        return redirect('administrador')
    return _wrapped_view

def check_only_operaciones(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.area == 'Operaciones':
            return view_func(request, *args, **kwargs)
        return redirect('administrador')
    return _wrapped_view

def check_for_pagadurias_aprobacion(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.area in ['Director', 'TI', 'Asesor', 'Coordinador', 'Riesgos', 'Financiero', 'Comercial']:
            return view_func(request, *args, **kwargs)
        return redirect('administrador')
    return _wrapped_view

def check_for_pagadurias(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.area in ['Director', 'TI', 'Asesor', 'Coordinador']:
            return view_func(request, *args, **kwargs)
        return redirect('administrador')
    return _wrapped_view

def check_for_update(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.area in ['Director', 'TI',]:
            return view_func(request, *args, **kwargs)
        return redirect('administrador')
    return _wrapped_view