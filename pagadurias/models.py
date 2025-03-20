from django.db import models
from .choicesDatas import *
import uuid

class Pagaduria(models.Model):

    # Datos de la Pagaduría - Empresa
    nombre = models.CharField(max_length=255, verbose_name="Nombre de la Pagaduría")
    razonSocial = models.CharField(max_length=200)
    sigla = models.CharField(max_length=200)
    nit = models.CharField(max_length=200)
    tipoEmpresa = models.CharField(max_length=100, choices=TIPOS_EMPRESA, verbose_name="Tipo de Empresa")
    actividadEconomica = models.CharField(max_length=200)
    
    # Asesores, controles y fecha de registro
    asesorCreated = models.CharField(max_length=200)
    asesorAsignado = models.CharField(max_length=200)
    fechaCreacion = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    tokenControl = models.UUIDField(default=uuid.uuid4(), editable=False, blank=True, null=True) # Eliminar blank y null
    
    # Estado final de aprovacion
    estado = models.CharField(max_length=200, default="Por aprobar", blank=True, null=True)
    # checkRiesgos = models.BooleanField()
    
    # Ubicación de la Pagaduría
    # pais = models.CharField(max_length=100, choices=PAISES)
    departamento = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    direccion = models.CharField(max_length=500)
    
    # Datos de la Pagaduría - Empleados
    totalEmpleados = models.IntegerField()
    empleadosIndefinidos = models.IntegerField()
    empleadosFijo = models.IntegerField()
    empleadosObraLabor = models.IntegerField()
    empleadosOtros = models.IntegerField()
    empleadosSalario1y2 = models.IntegerField()
    empleadosSalario2y4 = models.IntegerField()
    empleadosSalariomax4 = models.IntegerField()
    
    # Datos de la Pagaduría - Representante Legal
    nombreRepresentante = models.CharField(max_length=300)
    numeroCedulaRepresentante = models.IntegerField()
    correoRepresentante = models.EmailField()
    telefono = models.IntegerField()
    cedulaRepresentante = models.FileField(upload_to='files/')
    
    # Datos de la Pagaduría - Visación
    visacionLibranza = models.CharField(max_length=5, choices=VISACION)
    visacionMedio = models.CharField(max_length=20, choices=MEDIOVISACION)
    maxDescuentoNomina = models.FloatField()
    fechaMaxEnvioCuentaCobro = models.CharField(max_length=10, choices=FECHAENVIOCUENTAS)

    # Datos de la Pagaduría - Encargados Visacion
    encargadoVisacionNombre = models.CharField(max_length=200)
    encargadoVisacionCargo = models.CharField(max_length=200)
    encargadoVisacionCorreo = models.EmailField()
    encargadoVisacionTelefono = models.IntegerField()
    encargadoVisacionDireccion = models.CharField(max_length=400)
    
    # Datos de la pagaduria Envio Cuenta de Cobro
    encargadoEnvioCuentaNombre = models.CharField(max_length=200)
    encargadoEnvioCuentaCargo = models.CharField(max_length=200)
    encargadoEnvioCuentaCorreo = models.EmailField()
    encargadoEnvioCuentaTelefono = models.IntegerField()
    encargadoEnvioCuentaDireccion = models.CharField(max_length=400)
    
    # Documentos 
    convenio = models.FileField(upload_to='files/')
    formulariovinculacion = models.FileField(upload_to='files/')
    tarjetasFirma = models.FileField(upload_to='files/')
    rut = models.FileField(upload_to='files/')
    camaraComercio = models.FileField(upload_to='files/')
    estadosFinancieros = models.FileField(upload_to='files/')
    declaracionRenta = models.FileField(upload_to='files/')
    centrales = models.FileField(upload_to='files/')
    composicionAccionaria = models.FileField(upload_to='files/')
    
    
    # Estados de aprobación
    estadoFinanciero = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Pendiente')
    observacionFinanciero = models.TextField(null=True, blank=True)
    scoreFinanciero = models.FileField(upload_to='files/', null=True, blank=True)
    
    estadoComercial = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Pendiente')
    observacionComercial = models.TextField(null=True, blank=True)
    scoreComercial = models.FileField(upload_to='files/', null=True, blank=True)
    
    estadoRiesgos = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Pendiente')
    observacionRiesgos = models.TextField(null=True, blank=True)
    analisisRiesgos = models.FileField(upload_to='files/', null=True, blank=True)
    
    
    def save(self, *args, **kwargs):
        if self.estadoFinanciero == 'Aprobado' and self.estadoComercial == 'Aprobado' and self.estadoRiesgos == 'Aprobado':
            self.estado = 'Aprobado'
        else:
            self.estado = 'Por aprobar'
        super(Pagaduria, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre

