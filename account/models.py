from django.db import models
from django.contrib.auth.models import AbstractUser

TYPES_AREA = (
    ('Financiero', 'Financiero'),
    ('Comercial', 'Comercial'),
    ('Riesgos', 'Riesgos'),
    ('Asesor', 'Asesor'),
    ('Director', 'Director'),
    ('TI', 'TI'),
)

class User(AbstractUser):
    area = models.CharField(max_length=200, choices=TYPES_AREA, default='Asesor', blank=True, null=True)
    checkForTI = models.BooleanField(default=False)
    cedula = models.IntegerField(blank=True, null=True)