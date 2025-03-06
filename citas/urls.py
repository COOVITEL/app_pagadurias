from django.urls import path
from .views import citas_programadas, programar_cita

urlpatterns = [
    path('citas/', citas_programadas, name='citas_programadas'),
    path("programar_citas/", programar_cita, name="programar_cita"),
]
