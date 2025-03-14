from django.contrib import admin
from .models import CitaProgramada

# Register your models here.

@admin.register(CitaProgramada)
class CitaProgramadaAdmin(admin.ModelAdmin):
    list_display = ('pagaduria', 'asesor', 'fecha', 'hora', 'estado')
    list_filter = ('estado', 'fecha', 'pagaduria')
    search_fields = ('pagaduria__nombre', 'asesor')
    date_hierarchy = 'fecha'
    ordering = ('-fecha', 'hora')
