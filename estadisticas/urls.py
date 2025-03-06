from django.urls import path
from .views import estadisticas

urlpatterns = [
    path('estadisticas/', estadisticas, name='estadisticas'),
]
