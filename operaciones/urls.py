from django.urls import path
from .views import lista_operaciones  # Importar la vista

urlpatterns = [
    path('operaciones/', lista_operaciones, name='lista_operaciones'),
]
