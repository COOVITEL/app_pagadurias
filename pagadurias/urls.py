from django.urls import path
from . import views

urlpatterns = [
    path('pagaduriasAprobacion/', views.pagaduriasAprobacion, name='pagaduriasAprobacion'),
    path('pagadurias/', views.pagadurias, name='pagadurias'),
    path('registar-pagaduria/', views.createPagaduria, name="createPagaduria"),
    path('update-pagaduria/<int:id>/<str:token>/', views.updatePagaduria, name="updatePagaduria"),
    path('pagaduria/<int:pagaduria_id>/', views.info_pagaduria, name='info_pagaduria'),
    path('descargar-archivo/<int:pagaduria_id>/<str:field_name>/', views.descargar_archivo, name='descargar_archivo'),
    path('check-financiero/<str:name>/<str:token>/', views.check_financiero, name='check_financiero'),
    path('check-riesgos/<str:name>/<str:token>/', views.check_riesgos, name='check_riesgos'),
    path('check-comercial/<str:name>/<str:token>/', views.check_comercial, name='check_comercial'),
    path('revision-rechazo/<str:name>/<str:token>/', views.check_rechazo, name='check_rechazo'),
    path('historial/<int:pagaduria_id>/', views.historial_pagaduria_view, name='historial_pagaduria'),
]