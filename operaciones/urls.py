from django.urls import path
from . import views

urlpatterns = [
    path('operaciones/', views.lista_operaciones, name='lista_operaciones'),
    path('operaciones/aprobar/<str:nombre>/<str:tokenControl>/', views.aprobar_operaciones, name='aprobar_operaciones'),
]
