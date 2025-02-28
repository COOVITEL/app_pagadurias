from django.db import models

class Pagaduria(models.Model):
    ESTADO_CHOICES = [
        ('Por aprobar', 'Por aprobar'),
        ('Aprobado', 'Aprobado'),
        ('Rechazado', 'Rechazado'),
    ]

    nombre = models.CharField(max_length=255, verbose_name="Nombre de la Pagaduría")
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    empleados = models.IntegerField(verbose_name="Número de Empleados")
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Por aprobar', verbose_name="Estado")
    asesor = models.CharField(max_length=255, verbose_name="Asesor Asignado")
    afiliados = models.IntegerField(verbose_name="Número de Afiliados", default=0)
    creditos = models.IntegerField(verbose_name="Número de Créditos", default=0)
    cdats = models.IntegerField(verbose_name="Número de CDATs", default=0)
    coviahorro = models.IntegerField(verbose_name="Número de Coviahorro", default=0)

    def __str__(self):
        return self.nombre
