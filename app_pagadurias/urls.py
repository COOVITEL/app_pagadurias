from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', include('administrador.urls')),
    path('', include('pagadurias.urls')),
    path('', include('citas.urls')),
    path('', include('account.urls')),
    path('', include('operaciones.urls')),
    path('', include('estadisticas.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Servir archivos de medios en desarrollo
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
