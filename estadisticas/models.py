from django.db import models
from operaciones.models import Operacion  # Asegúrate de que la app "operaciones" exista

class Estadistica(models.Model):
    operacion = models.ForeignKey(Operacion, on_delete=models.CASCADE, related_name="estadisticas")
    fecha_generacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Generación")
    total_creditos = models.IntegerField(default=0, verbose_name="Total de Créditos")
    total_cdats = models.IntegerField(default=0, verbose_name="Total de CDATs")
    total_coviahorro = models.IntegerField(default=0, verbose_name="Total de Coviahorro")
    
    def __str__(self):
        return f"Estadística de {self.operacion} - {self.fecha_generacion.strftime('%Y-%m-%d')}"
