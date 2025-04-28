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