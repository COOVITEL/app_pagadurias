from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from account.models import User

def check_authoritation(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "❌ No estás autenticado.")
            return redirect('login')  

        if not request.user.checkForTI:
            ti_emails = User.objects.filter(area='TI', is_active=True).values_list('email', flat=True)
            if ti_emails:
                subject = "🔒 Solicitud de autorización para usuario no autorizado"
                html_content = render_to_string('emails/nuevo_usuario.html', {
                    'usuario': request.user,
                    'mensaje': "Este usuario intentó acceder a una función para la cual no está autorizado.",
                })
                send_mail(
                    subject,
                    '',
                    settings.DEFAULT_FROM_EMAIL,
                    list(ti_emails),
                    fail_silently=False,
                    html_message=html_content
                )
            messages.error(request, "❌ No estás autorizado para realizar esta acción. Se ha notificado al equipo de TI.")
            return redirect('login')  

        return view_func(request, *args, **kwargs)
    return wrapper

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