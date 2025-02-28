from django.contrib import admin
from django.urls import path, include
from pagadurias.views import pagaduriasAprobacion, pagadurias

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', include('administrador.urls')),
    path('pagaduriasAprobacion/', pagaduriasAprobacion, name='pagaduriasAprobacion'),
    path('pagadurias/', pagadurias, name='pagadurias'),
]
