from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from account.decorators import check_authoritation
from django.shortcuts import get_object_or_404
from account.models import User
from django.contrib import messages
from account.utils import NotificacionUsuarioService



@login_required
@check_authoritation
def waiting_for_auth(request):
    if request.user.checkForTI:
        return redirect("/")
    return render(request, 'waiting_for_auth.html')

@login_required
def autorizar_usuario(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if not user.checkForTI:  # Verifica si el usuario aún no está autorizado
        user.checkForTI = True
        user.save()

        try:
            NotificacionUsuarioService.notificar_autorizacion(user)
            messages.success(request, f"El usuario {user.username} ha sido autorizado y notificado.")
        except Exception as e:
            messages.error(request, f"Error al enviar la notificación: {e}")
    else:
        messages.info(request, f"El usuario {user.username} ya estaba autorizado.")

    return redirect('asesores')
