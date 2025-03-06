
from django.db import models

class Operacion(models.Model):
    pagaduria = models.CharField(max_length=255)
    asesor = models.CharField(max_length=255)
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.pagaduria} - {self.fecha} {self.hora}"
