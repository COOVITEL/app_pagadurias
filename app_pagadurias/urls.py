from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', include('administrador.urls')),
    path('', include('pagadurias.urls')),
    path('', include('citas.urls')),
    path('', include('account.urls')),
]
