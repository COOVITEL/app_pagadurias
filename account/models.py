from django.db import models
from django.contrib.auth.models import AbstractUser

TYPES_AREA = (
    ('Financiero', 'Financiero'),
    ('Comercial', 'Comercial'),
    ('Riesgos', 'Riesgos'),
    ('Asesor', 'Asesor'),
    ('Coordinador', 'Coordinador'),
    ('Director', 'Director'),
    ('TI', 'TI'),
    ('Operaciones', 'Operaciones'),
)

class User(AbstractUser):
    area = models.CharField(max_length=200, choices=TYPES_AREA, default='Asesor', blank=True, null=True)
    checkForTI = models.BooleanField(default=False)
    cedula = models.IntegerField(blank=True, null=True)
    
    def numPagadurias(self):
        return self.pagaduria.count()
    
    def nameComplate(self):
        return f"{self.first_name} {self.last_name}"
    
    def allowedOperaciones(self):
        return self.area in ['Director', 'TI', 'Operaciones']
    
    def allowedRiesgosFinanComer(self):
        return self.area in ['Director', 'TI', 'Riesgos', 'Financiero', 'Comercial', 'Coordinador']
    
    def allowedDirTiCoor(self):
        return self.area in ['Director', 'TI', 'Coordinador']
    
    def allowedAsesor(self):
        return self.area == "Asesor"
    

