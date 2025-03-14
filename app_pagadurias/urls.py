from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', include('administrador.urls')),
    path('', include('pagadurias.urls')),
    path('', include('citas.urls', namespace='citas')),
    path('', include('account.urls')),
    path('', include('operaciones.urls')),
    path('', include('estadisticas.urls')),
]
