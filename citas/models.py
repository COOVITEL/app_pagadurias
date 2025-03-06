from django.db import models

class Pagaduria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Asesor(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class CitaProgramada(models.Model):
    pagaduria = models.ForeignKey(Pagaduria, on_delete=models.CASCADE)
    asesor = models.ForeignKey(Asesor, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.asesor} - {self.fecha} {self.hora}"
