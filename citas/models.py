from django.db import models

class CitaProgramada(models.Model):
    pagaduria = models.CharField(max_length=255, verbose_name="Pagaduría")
    asesor = models.CharField(max_length=255, verbose_name="Asesor Asignado")
    fecha = models.DateField(verbose_name="Fecha de la Cita")
    hora = models.TimeField(verbose_name="Hora de la Cita")

    def __str__(self):
        return f"{self.pagaduria} - {self.fecha} {self.hora}"
