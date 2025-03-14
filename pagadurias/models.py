from django.db import models
from .choicesDatas import *

class Pagaduria(models.Model):

    # Datos de la Pagaduría - Empresa
    nombre = models.CharField(max_length=255, verbose_name="Nombre de la Pagaduría")
    fechaCreacion = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    razonSocial = models.CharField(max_length=200)
    sigla = models.CharField(max_length=200)
    nit = models.CharField(max_length=200)
    tipoEmpresa = models.CharField(max_length=100, choices=TIPOS_EMPRESA, verbose_name="Tipo de Empresa")
    actividadEconomica = models.CharField(max_length=200)
    #
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
    
    # def save(self, *args, **kwargs):
    #     if not self.convenio:
    #         self.convenio = 
    #     super(Pagaduria, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre

