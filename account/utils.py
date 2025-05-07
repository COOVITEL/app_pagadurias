from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from account.models import User
from django.core.mail import send_mail

class NotificacionUsuarioService:

    #@staticmethod
    #def notificar_a_ti(usuario):
    #    subject = "🚨 Nuevo usuario pendiente de autorización"
    #    html_content = render_to_string('emails/nuevo_usuario.html', {'usuario': usuario})
    #    destinatarios = ['ti@tuempresa.com']
    #    NotificacionUsuarioService._enviar(subject, html_content, destinatarios)

    @staticmethod
    def notificar_autorizacion(user):
        """
        Envía una notificación por correo electrónico al usuario cuando es autorizado.
        """
        try:
            subject = "✅ Usuario autorizado"
            html_content = render_to_string('emails/usuario_autorizado.html', {'usuario': user})
            destinatarios = [user.email]

            # Verifica que el usuario tenga un correo válido
            if not user.email:
                raise ValueError(f"El usuario {user.username} no tiene un correo electrónico válido.")

            # Llama al método para enviar el correo
            NotificacionUsuarioService._enviar(subject, html_content, destinatarios)
        except Exception as e:
            # Manejo de errores: registra el error o muestra un mensaje
            print(f"Error al enviar la notificación al usuario {user.username}: {e}")

    @staticmethod
    def _enviar(subject, html_content, destinatarios):
        """
        Método interno para enviar correos electrónicos utilizando send_mail.
        """
        try:
            print("➡️ Entrando a _enviar()")
            print(f"Destinatarios: {destinatarios}")
            print(f"Subject: {subject}")

            if not settings.DEFAULT_FROM_EMAIL:
                raise ValueError("DEFAULT_FROM_EMAIL no está configurado en settings.py")

            message = EmailMultiAlternatives(subject, '', settings.DEFAULT_FROM_EMAIL, destinatarios)
            message.attach_alternative(html_content, "text/html")
            message.send()
            print("✅ Correo enviado exitosamente")
        except Exception as e:
            print(f"❌ Error al enviar el correo: {e}")

        