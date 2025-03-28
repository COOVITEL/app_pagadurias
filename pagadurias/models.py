from django.db import models
from .choicesDatas import *
import uuid

class Pagaduria(models.Model):

    # Datos de la Pagaduría - Empresa
    nombre = models.CharField(max_length=255, verbose_name="Nombre de la Pagaduría")
    razonSocial = models.CharField(max_length=200, blank=True, null=True)
    sigla = models.CharField(max_length=200, blank=True, null=True)
    nit = models.CharField(max_length=200)
    tipoEmpresa = models.CharField(max_length=100, choices=TIPOS_EMPRESA, verbose_name="Tipo de Empresa", blank=True, null=True)
    actividadEconomica = models.CharField(max_length=200, blank=True, null=True)
    
    # Asesores, controles y fecha de registro
    asesorCreated = models.CharField(max_length=200, blank=True, null=True)
    asesorAsignado = models.CharField(max_length=200, blank=True, null=True)
    fechaCreacion = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación", blank=True, null=True)
    tokenControl = models.UUIDField(default=uuid.uuid4(), editable=False, blank=True, null=True) # Eliminar blank y null
    
    # Estado final de aprovacion
    estado = models.CharField(max_length=200, default="Por aprobar", blank=True, null=True)
    # checkRiesgos = models.BooleanField()
    
    # Ubicación de la Pagaduría
    # pais = models.CharField(max_length=100, choices=PAISES)
    departamento = models.CharField(max_length=200, blank=True, null=True)
    ciudad = models.CharField(max_length=200, blank=True, null=True)
    direccion = models.CharField(max_length=500, blank=True, null=True)
    
    # Datos de la Pagaduría - Empleados
    totalEmpleados = models.IntegerField(blank=True, null=True)
    empleadosIndefinidos = models.IntegerField(blank=True, null=True)
    empleadosFijo = models.IntegerField(blank=True, null=True)
    empleadosObraLabor = models.IntegerField(blank=True, null=True)
    empleadosOtros = models.IntegerField(blank=True, null=True)
    empleadosSalario1y2 = models.IntegerField(blank=True, null=True)
    empleadosSalario2y4 = models.IntegerField(blank=True, null=True)
    empleadosSalariomax4 = models.IntegerField(blank=True, null=True)
    
    # Datos de la Pagaduría - Representante Legal
    nombreRepresentante = models.CharField(max_length=300, blank=True, null=True)
    numeroCedulaRepresentante = models.CharField(max_length=200, blank=True, null=True)
    correoRepresentante = models.EmailField(blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    cedulaRepresentante = models.FileField(upload_to='files/', blank=True, null=True)
    
    # Datos de la Pagaduría - Visación
    visacionLibranza = models.CharField(max_length=5, choices=VISACION, blank=True, null=True)
    visacionMedio = models.CharField(max_length=20, choices=MEDIOVISACION, blank=True, null=True)
    maxDescuentoNomina = models.FloatField(blank=True, null=True)
    fechaMaxEnvioCuentaCobro = models.CharField(max_length=10, choices=FECHAENVIOCUENTAS, blank=True, null=True)

    # Datos de la Pagaduría - Encargados Visacion
    encargadoVisacionNombre = models.CharField(max_length=200, blank=True, null=True)
    encargadoVisacionCargo = models.CharField(max_length=200, blank=True, null=True)
    encargadoVisacionCorreo = models.EmailField(blank=True, null=True)
    encargadoVisacionTelefono = models.IntegerField(blank=True, null=True)
    encargadoVisacionDireccion = models.CharField(max_length=400, blank=True, null=True)
    
    # Datos de la pagaduria Envio Cuenta de Cobro
    encargadoEnvioCuentaNombre = models.CharField(max_length=200, blank=True, null=True)
    encargadoEnvioCuentaCargo = models.CharField(max_length=200, blank=True, null=True)
    encargadoEnvioCuentaCorreo = models.EmailField(blank=True, null=True)
    encargadoEnvioCuentaTelefono = models.IntegerField(blank=True, null=True)
    encargadoEnvioCuentaDireccion = models.CharField(max_length=400, blank=True, null=True)
    
    # Documentos 
    convenio = models.FileField(upload_to='files/', blank=True, null=True)
    formulariovinculacion = models.FileField(upload_to='files/', blank=True, null=True)
    tarjetasFirma = models.FileField(upload_to='files/', blank=True, null=True)
    rut = models.FileField(upload_to='files/', blank=True, null=True)
    camaraComercio = models.FileField(upload_to='files/', blank=True, null=True)
    estadosFinancieros = models.FileField(upload_to='files/', blank=True, null=True)
    declaracionRenta = models.FileField(upload_to='files/', blank=True, null=True)
    centrales = models.FileField(upload_to='files/', blank=True, null=True)
    composicionAccionaria = models.FileField(upload_to='files/', blank=True, null=True)
    
    
    # Estados de aprobación
    estadoFinanciero = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Pendiente')
    observacionFinanciero = models.TextField(null=True, blank=True)
    scoreFinanciero = models.FileField(upload_to='files/', null=True, blank=True)

    estadoRiesgos = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Pendiente')
    observacionRiesgos = models.TextField(null=True, blank=True)
    analisisRiesgos = models.FileField(upload_to='files/', null=True, blank=True)
    
    estadoComercial = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado')], default='Pendiente')
    observacionComercial = models.TextField(null=True, blank=True)
    scoreComercial = models.FileField(upload_to='files/', null=True, blank=True)   
    
    def save(self, *args, **kwargs):
        if self.estadoFinanciero == 'Aprobado' and self.estadoComercial == 'Aprobado' and self.estadoRiesgos == 'Aprobado':
            self.estado = 'Aprobado'
        else:
            self.estado = 'Por aprobar'
        super(Pagaduria, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre

