from django.urls import path
from .views import citas_programadas

urlpatterns = [
    path('citas/', citas_programadas, name='citas_programadas'),
]
