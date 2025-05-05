from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime, time
from pagadurias.models import Pagaduria
from account.models import User


class CitaProgramada(models.Model):
    ESTADO_CHOICES = [
        ('Programada', 'Programada'),
        ('Completada', 'Completada'),
        ('Cancelada', 'Cancelada'),
        ('En atención', 'En atención')
    ]

    pagaduria = models.ForeignKey(Pagaduria, on_delete=models.CASCADE,verbose_name="Pagaduría")
    asesor = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Asesor")
    fecha = models.DateField(verbose_name="Fecha")
    hora = models.TimeField(verbose_name="Hora")
    estado = models.CharField(max_length=20,choices=ESTADO_CHOICES,default='Programada',verbose_name="Estado")
    fecha_creacion = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    ultima_modificacion = models.DateTimeField(auto_now=True,verbose_name="Última modificación")
    notas = models.TextField(blank=True,null=True,verbose_name="Notas")
    resultado = models.TextField(blank=True,null=True,verbose_name="resultado")


    def __str__(self):
        return f"{self.asesor} - {self.pagaduria} - {self.fecha} {self.hora}"

    def clean(self):
        # Validar que la fecha no sea en el pasado
        if self.fecha and self.fecha < timezone.now().date():
            raise ValidationError({'fecha': 'No se pueden programar citas en fechas pasadas'})

        # Validar que no sea fin de semana
        if self.fecha and self.fecha.weekday() >= 5:
            raise ValidationError({'fecha': 'No se pueden programar citas en fin de semana'})

        # Validar horario de atención (8:00 AM - 5:00 PM)
        if self.hora:
            hora_min = time(8, 0)  # 8:00 AM
            hora_max = time(17, 0)  # 5:00 PM
            if self.hora < hora_min or self.hora > hora_max:
                raise ValidationError({
                    'hora': 'Las citas solo se pueden programar entre 8:00 AM y 5:00 PM'
                })

        # Validar que no haya otra cita en la misma fecha y hora
        if self.fecha and self.hora:
            citas_existentes = CitaProgramada.objects.filter(
                fecha=self.fecha,
                hora=self.hora
            )
            if self.pk:  # Si es una actualización, excluir la cita actual
                citas_existentes = citas_existentes.exclude(pk=self.pk)
            if citas_existentes.exists():
                raise ValidationError({
                    'hora': 'Ya existe una cita programada para esta fecha y hora'
                })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
