from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

class NotificacionUsuarioService:

    @staticmethod
    def notificar_a_ti(usuario):
        subject = "🚨 Nuevo usuario pendiente de autorización"
        html_content = render_to_string('emails/nuevo_usuario.html', {'usuario': usuario})
        destinatarios = ['ti@tuempresa.com']
        NotificacionUsuarioService._enviar(subject, html_content, destinatarios)

    @staticmethod
    def notificar_autorizacion(usuario):
        subject = "✅ Usuario autorizado"
        html_content = render_to_string('emails/usuario_autorizado.html', {'usuario': usuario})
        destinatarios = [usuario.email]
        NotificacionUsuarioService._enviar(subject, html_content, destinatarios)

    @staticmethod
    def _enviar(subject, html_content, destinatarios):
        message = EmailMultiAlternatives(subject, '', settings.DEFAULT_FROM_EMAIL, destinatarios)
        message.attach_alternative(html_content, "text/html")
        message.send()
