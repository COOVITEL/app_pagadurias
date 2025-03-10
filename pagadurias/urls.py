from django.urls import path
from .views import *

urlpatterns = [
    path('pagaduriasAprobacion/', pagaduriasAprobacion, name='pagaduriasAprobacion'),
    path('pagadurias/', pagadurias, name='pagadurias'),
    path('registar-pagaduria/', createPagaduria, name="createPagaduria")
]