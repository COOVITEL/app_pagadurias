from django.urls import path, include
from .views import *

urlpatterns = [
    path('', administrador, name="administrador"),
    path('linix/', callAndUpdatePagaduriasExistLinix, name="callAndUpdatePagaduriasExistLinix"),
]
