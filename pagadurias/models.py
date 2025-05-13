from django.db import models
from .choicesDatas import *
import uuid
from dotenv import load_dotenv
import os
from account.models import User
from django.db.models import Sum

load_dotenv()

class Pagaduria(models.Model):
    
    CHOISE_STATUS = [
        ('Pendiente', 'Pendiente'),
        ('Aprobado', 'Aprobado'),
        ('Rechazado por Politicas', 'Rechazado por Politicas'),
        ('Rechazado por Documentación', 'Rechazado por Documentación'),
        ]

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
    departamento = models.CharField(max_length=200, blank=True, null=True)
    ciudad = models.CharField(max_length=200, blank=True, null=True)
    direccion = models.CharField(max_length=500, blank=True, null=True)
    
    # Datos de la Pagaduría - Representante Legal
    nombreRepresentante = models.CharField(max_length=300, blank=True, null=True)
    numeroCedulaRepresentante = models.CharField(max_length=200, blank=True, null=True)
    correoRepresentante = models.EmailField(blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    cedulaRepresentante = models.FileField(upload_to='cedulaRepre/', blank=True, null=True)
    
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
    convenio = models.FileField(upload_to='convenio/', blank=True, null=True)
    formulariovinculacion = models.FileField(upload_to='formVinculacion/', blank=True, null=True)
    tarjetasFirma = models.FileField(upload_to='tarjetasFirma/', blank=True, null=True)
    rut = models.FileField(upload_to='rut/', blank=True, null=True)
    camaraComercio = models.FileField(upload_to='camaraComercio/', blank=True, null=True)
    estadosFinancieros = models.FileField(upload_to='estadosFinancieros/', blank=True, null=True)
    declaracionRenta = models.FileField(upload_to='declaRenta/', blank=True, null=True)
    centrales = models.FileField(upload_to='centrales/', blank=True, null=True)
    composicionAccionaria = models.FileField(upload_to='comAccionaria/', blank=True, null=True)
    
    
    # Estados de aprobación
    estadoComercial = models.CharField(max_length=30, choices=CHOISE_STATUS, default='Pendiente')
    observacionComercial = models.TextField(null=True, blank=True)
    scoreComercial = models.FileField(upload_to='scoreComercial/', null=True, blank=True)
    
    estadoFinanciero = models.CharField(max_length=30, choices=CHOISE_STATUS, default='Pendiente')
    observacionFinanciero = models.TextField(null=True, blank=True)
    scoreFinanciero = models.FileField(upload_to='scoreFinanciero/', null=True, blank=True)

    estadoRiesgos = models.CharField(max_length=30, choices=CHOISE_STATUS, default='Pendiente')
    observacionRiesgos = models.TextField(null=True, blank=True)
    analisisRiesgos = models.FileField(upload_to='analisisRiesgos/', null=True, blank=True)
    
    estadoOperaciones = models.BooleanField(default=False)
    asesores = models.ManyToManyField(User, related_name='pagaduria')
    
    
    
    def save(self, *args, **kwargs):
        if self.estadoFinanciero == 'Aprobado' and self.estadoComercial == 'Aprobado' and self.estadoRiesgos == 'Aprobado':
            self.estado = 'Aprobado'
        else:
            self.estado = 'Por aprobar'
        super(Pagaduria, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre
    
    def checkRechazoFinanciero(self, user):
        return str(self.asesorCreated) == str(user) and self.estadoFinanciero == 'Rechazado'
    
    def pathCedulaRepresentante(self):
        ruta = f"{os.getenv('DOMINIO')}{self.cedulaRepresentante}"
        return ruta
    
    def pathConvenio(self):
        ruta = f"{os.getenv('DOMINIO')}{self.convenio}"
        return ruta
    def pathFormulariovinculacion(self):
        ruta = f"{os.getenv('DOMINIO')}{self.formulariovinculacion}"
        return ruta
    def pathTajetasfirma(self):
        ruta = f"{os.getenv('DOMINIO')}{self.tarjetasFirma}"
        return ruta
    def pathRut(self):
        ruta = f"{os.getenv('DOMINIO')}{self.rut}"
        return ruta
    def pathCamaraComercio(self):
        ruta = f"{os.getenv('DOMINIO')}{self.camaraComercio}"
        return ruta
    def pathEstadosFinancieros(self):
        ruta = f"{os.getenv('DOMINIO')}{self.estadosFinancieros}"
        return ruta
    def pathDeclaracionRenta(self):
        ruta = f"{os.getenv('DOMINIO')}{self.declaracionRenta}"
        return ruta
    def pathCentrales(self):
        ruta = f"{os.getenv('DOMINIO')}{self.centrales}"
        return ruta
    def pathComposicionAccionaria(self):
        ruta = f"{os.getenv('DOMINIO')}{self.composicionAccionaria}"
        return ruta
    
    def buscarRechazo(self):
        if self.estadoFinanciero == "Rechazado" or self.estadoComercial == "Rechazado" or self.estadoFinanciero == "Rechazado":
            return True
        return False

    def totalEmpleados(self):
        total = self.sucursales.aggregate(totalEmpleados=Sum('totalEmpleados'))['totalEmpleados'] or 0
        return str(total)



class SucursalesPagaduria(models.Model):
    pagaduria = models.ForeignKey(Pagaduria, on_delete=models.CASCADE, related_name='sucursales')
    departamento = models.CharField(max_length=200, blank=True, null=True)
    ciudad = models.CharField(max_length=200, blank=True, null=True)
    totalEmpleados = models.IntegerField(blank=True, null=True)
    empleadosIndefinidos = models.IntegerField(blank=True, null=True)
    empleadosFijo = models.IntegerField(blank=True, null=True)
    empleadosObraLabor = models.IntegerField(blank=True, null=True)
    empleadosOtros = models.IntegerField(blank=True, null=True)
    empleadosSalario1y2 = models.IntegerField(blank=True, null=True)
    empleadosSalario2y4 = models.IntegerField(blank=True, null=True)
    empleadosSalariomax4 = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.pagaduria.nombre} - {self.id}"


class ObservacionesPagaduria(models.Model):
    pagaduria = models.ForeignKey(Pagaduria, related_name='observacion', on_delete=models.CASCADE)
    area = models.CharField(max_length=200, blank=True, null=True)
    observacion = models.TextField(max_length=2000)
    fecha = models.DateField(auto_now_add=True)
    creadoPor = models.CharField(max_length=200)


class HistorialPagaduria(models.Model):
    pagaduria = models.ForeignKey('Pagaduria', on_delete=models.CASCADE)
    accion = models.CharField(max_length=50, choices=ACCION_CHOICES)
    descripcion = models.TextField()
    realizado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.pagaduria.nombre} - {self.get_accion_display()} ({self.fecha})"
    
    