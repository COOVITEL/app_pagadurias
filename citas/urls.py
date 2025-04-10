from django.urls import path
from . import views

urlpatterns = [
    path('citas/', views.citas_programadas, name='citas_programadas'),
    path('citas/programar/', views.programar_cita, name='programar_cita'),
    path('citas/editar/<int:cita_id>/', views.editar_cita, name='editar_cita'),
    path('citas/eliminar/<int:cita_id>/', views.eliminar_cita, name='eliminar_cita'),
]
