from django.urls import path
from .views import pagaduriasAprobacion, pagadurias

urlpatterns = [
    path('pagaduriasAprobacion/', pagaduriasAprobacion, name='pagaduriasAprobacion'),
    path('pagadurias/', pagadurias, name='pagadurias'),
]