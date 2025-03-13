from django import forms
from .models import Pagaduria

class PagaduriaForm(forms.ModelForm):
  class Meta:
    model = Pagaduria
    fields = [
      'nombre', 'razonSocial', 'sigla', 'nit', 'tipoEmpresa',
      'actividadEconomica', 'estado', 'departamento',
      'ciudad', 'direccion', 'totalEmpleados',
      'empleadosIndefinidos', 'empleadosFijo',
      'empleadosObraLabor', 'empleadosOtros', 'empleadosSalario1y2',
      'empleadosSalario2y4', 'empleadosSalariomax4', 'nombreRepresentante',
      'cedulaRepresentante', 'correoRepresentante', 'telefono',
      'visacionLibranza', 'visacionMedio', 'maxDescuentoNomina',
      'fechaMaxEnvioCuentaCobro', 'encargadoVisacionNombre',
      'encargadoVisacionCargo', 'encargadoVisacionCorreo',
      'encargadoVisacionTelefono', 'encargadoVisacionDireccion',
      'encargadoEnvioCuentaNombre', 'encargadoEnvioCuentaCargo',
      'encargadoEnvioCuentaCorreo', 'encargadoEnvioCuentaTelefono',
      'encargadoEnvioCuentaDireccion'
    ]
    labels = {
            'nombre': 'Nombre de la Pagaduría',
            'razonSocial': 'Razón Social',
            'sigla': 'Sigla',
            'nit': 'NIT',
            'tipoEmpresa': 'Tipo de Empresa',
            'actividadEconomica': 'Actividad Económica',
            'estado': 'Estado',
            'departamento': 'Departamento',
            'ciudad': 'Ciudad',
            'direccion': 'Dirección',
            'totalEmpleados': 'Total de Empleados',
            'empleadosIndefinidos': 'Empleados Indefinidos',
            'empleadosFijo': 'Empleados Fijos',
            'empleadosObraLabor': 'Empleados por Obra o Labor',
            'empleadosOtros': 'Otros Empleados',
            'empleadosSalario1y2': 'Empleados con Salario entre 1 y 2 SMMLV',
            'empleadosSalario2y4': 'Empleados con Salario entre 2 y 4 SMMLV',
            'empleadosSalariomax4': 'Empleados con Salario Mayor a 4 SMMLV',
            'nombreRepresentante': 'Nombre del Representante Legal',
            'cedulaRepresentante': 'Cédula del Representante Legal',
            'correoRepresentante': 'Correo del Representante Legal',
            'telefono': 'Teléfono de Contacto',
            'visacionLibranza': 'Visación de Libranza',
            'visacionMedio': 'Medio de Visación',
            'maxDescuentoNomina': 'Máximo Descuento por Nómina',
            'fechaMaxEnvioCuentaCobro': 'Fecha Máxima de Envío de Cuenta de Cobro',
            'encargadoVisacionNombre': 'Nombre del Encargado de Visación',
            'encargadoVisacionCargo': 'Cargo del Encargado de Visación',
            'encargadoVisacionCorreo': 'Correo del Encargado de Visación',
            'encargadoVisacionTelefono': 'Teléfono del Encargado de Visación',
            'encargadoVisacionDireccion': 'Dirección del Encargado de Visación',
            'encargadoEnvioCuentaNombre': 'Nombre del Encargado de Envío de Cuenta',
            'encargadoEnvioCuentaCargo': 'Cargo del Encargado de Envío de Cuenta',
            'encargadoEnvioCuentaCorreo': 'Correo del Encargado de Envío de Cuenta',
            'encargadoEnvioCuentaTelefono': 'Teléfono del Encargado de Envío de Cuenta',
            'encargadoEnvioCuentaDireccion': 'Dirección del Encargado de Envío de Cuenta',
        }

    # widget = {
    #   'empleadosSalario1y2': forms.TextInput(attrs={'class': 'long'}),
    #   'empleadosSalario2y4': forms.TextInput(attrs={'class': 'long'}),
    #   'empleadosSalariomax4': forms.TextInput(attrs={'class': 'long'}),
    # }
  
  # def __init__(self, *args, **kwargs):
  #   super().__init__(*args, **kwargs)
  #   self.fields['empleadosSalario1y2'].label_attrs = {'class': 'long'}