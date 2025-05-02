from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .models import HistorialPagaduria,  ObservacionesPagaduria
import requests

def getDepartamentAndCitys() -> list:
    """
        Get the list of departments and cities in Colombia from the API.
        Params:
            url (str): The URL of the API endpoint.
        Returns:
            List[Dict]: A list of dictionaries containing department and city information.
    """
    try:
        url = "https://www.datos.gov.co/resource/xdk5-pm3f.json"
        datas = requests.get(url)
        departamentos = set([dep['departamento'] for dep in datas.json()])
        ciudades = [f"{dep['departamento']}-{dep['municipio']}" for dep in datas.json()]
        return [departamentos, ciudades]
    
    except requests.exceptions.RequestException as e:
        print(e)
        

class EmailService:

    @staticmethod
    def enviar_creacion_pagaduria(pagaduria, destinatarios):
        subject = f"📌 Nueva pagaduría creada: {pagaduria.nombre}"
        html_content = render_to_string('emails/creacion_pagaduria.html', {'pagaduria': pagaduria})
        EmailService._enviar_correo(subject, html_content, destinatarios)

    @staticmethod
    def enviar_actualizacion_pagaduria(pagaduria, destinatarios):
        subject = f"✏️ Pagaduría actualizada: {pagaduria.nombre}"
        html_content = render_to_string('emails/actualizacion_pagaduria.html', {'pagaduria': pagaduria})
        EmailService._enviar_correo(subject, html_content, destinatarios)

    @staticmethod
    def enviar_cambio_estado(pagaduria, destinatarios):
        subject = f"⚠️ Estado actualizado: {pagaduria.nombre}"
        html_content = render_to_string('emails/cambio_estado_pagaduria.html', {'pagaduria': pagaduria})
        EmailService._enviar_correo(subject, html_content, destinatarios)   

    @staticmethod
    def _enviar_correo(subject, html_content, destinatarios):
        message = EmailMultiAlternatives(subject, '', settings.DEFAULT_FROM_EMAIL, destinatarios)
        message.attach_alternative(html_content, "text/html")
        message.send(fail_silently=False)

 
class HistorialService:
    @staticmethod
    def registrar_historial(pagaduria, accion, descripcion=None, realizado_por=None):
        print(f"[DEBUG] Ejecutando historial: {accion} para {pagaduria.nombre}")

        if accion in ['aprobacion', 'rechazo']:
            ultima_obs = ObservacionesPagaduria.objects.filter(pagaduria=pagaduria).order_by('-fecha').first()
            area = ultima_obs.area if ultima_obs else "desconocida"

            if accion == 'aprobacion':
                descripcion = f'Se aprobó la pagaduría {pagaduria.nombre} por el área de {area}'
            elif accion == 'rechazo':
                descripcion = f'Se rechazó la pagaduría {pagaduria.nombre} por el área de {area}'
        
        elif accion == 'creación':
            descripcion = f'Se creó la pagaduría {pagaduria.nombre}'
        elif accion == 'actualización':
            descripcion = f'Se actualizó la información de la pagaduría {pagaduria.nombre}'
        elif accion == 'cambio_estado':
            descripcion = f'Se cambió el estado de la pagaduría {pagaduria.nombre} a {pagaduria.estado}'
        else:
            descripcion = descripcion or "Acción no especificada."

        HistorialPagaduria.objects.create(
            pagaduria=pagaduria,
            accion=accion,
            descripcion=descripcion,
            realizado_por=realizado_por
        )

    
    @staticmethod
    def obtener_historial(pagaduria):
        return HistorialPagaduria.objects.filter(pagaduria=pagaduria).order_by('-fecha')
