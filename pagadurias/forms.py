from django import forms
from .models import Pagaduria, SucursalesPagaduria, ObservacionesPagaduria

class PagaduriaForm(forms.ModelForm):
  class Meta:
    model = Pagaduria
    fields = [
      'nombre', 'razonSocial', 'sigla', 'nit', 'tipoEmpresa',
      'actividadEconomica', 'estado', 'departamento',
      'ciudad', 'direccion',
      'nombreRepresentante',
      'numeroCedulaRepresentante', 'correoRepresentante', 'telefono', 'cedulaRepresentante',
      'visacionLibranza', 'visacionMedio', 'maxDescuentoNomina',
      'fechaMaxEnvioCuentaCobro', 'encargadoVisacionNombre',
      'encargadoVisacionCargo', 'encargadoVisacionCorreo',
      'encargadoVisacionTelefono', 'encargadoVisacionDireccion',
      'encargadoEnvioCuentaNombre', 'encargadoEnvioCuentaCargo',
      'encargadoEnvioCuentaCorreo', 'encargadoEnvioCuentaTelefono',
      'encargadoEnvioCuentaDireccion', 'convenio', 'formulariovinculacion',
      'tarjetasFirma', 'rut', 'camaraComercio', 'estadosFinancieros',
      'declaracionRenta', 'centrales', 'composicionAccionaria'
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
            # 'totalEmpleados': 'Total de Empleados',
            # 'empleadosIndefinidos': 'Empleados Indefinidos',
            # 'empleadosFijo': 'Empleados Fijos',
            # 'empleadosObraLabor': 'Empleados por Obra o Labor',
            # 'empleadosOtros': 'Otros Empleados',
            # 'empleadosSalario1y2': 'Empleados con Salario entre 1 y 2 SMMLV',
            # 'empleadosSalario2y4': 'Empleados con Salario entre 2 y 4 SMMLV',
            # 'empleadosSalariomax4': 'Empleados con Salario Mayor a 4 SMMLV',
            'nombreRepresentante': 'Nombre del Representante Legal',
            'numeroCedulaRepresentante': 'Numero Cédula del Representante Legal',
            'correoRepresentante': 'Correo del Representante Legal',
            'telefono': 'Teléfono de Contacto',
            'cedulaRepresentante': 'Cedula del Representante Legal',
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
            'convenio': 'Convenio',
            'formulariovinculacion': 'Formulario de Vinculación',
            'tarjetasFirma': 'Tarjeta de Firmas',
            'rut': 'RUT',
            'camaraComercio': 'Cámara de Comercio',
            'estadosFinancieros': 'Estados Financieros',
            'declaracionRenta': 'Declaración de Renta',
            'centrales': 'Centrales de Riesgo',
            'composicionAccionaria': 'Composición Accionaria'
        }

    # widgets = {
    #     'nombre': forms.TextInput(attrs={'class': 'form-control'}, required=True),
    # }
    # def clean_encargadoVisacionCargo(self):
    #     nombre = self.cleaned_data.get('encargadoVisacionCargo')
    #     if len(nombre) < 5:
    #         raise forms.ValidationError("El encargadoVisacionCargo de la Pagaduría debe tener al menos 5 caracteres")
    #     return nombre

class SucursalForm(forms.ModelForm):
  class Meta:
    model = SucursalesPagaduria
    fields = [
      'departamento',
      'ciudad',
      'totalEmpleados',
      'empleadosIndefinidos',
      'empleadosFijo',
      'empleadosObraLabor',
      'empleadosOtros',
      'empleadosSalario1y2',
      'empleadosSalario2y4',
      'empleadosSalariomax4'
      ]
    widgets = {
      'departamento': forms.Select(attrs={
          'class': 'w-full text-center',
      }),
      'ciudad': forms.Select(attrs={
          'class': 'w-full text-center',
      }),
      'totalEmpleados': forms.NumberInput(attrs={
          'class': 'w-full text-center',
      }),
      'empleadosIndefinidos': forms.NumberInput(attrs={
          'class': 'w-full text-center',
      }),
      'empleadosFijo': forms.NumberInput(attrs={
          'class': 'w-full text-center',
      }),
      'empleadosObraLabor': forms.NumberInput(attrs={
          'class': 'w-full text-center',
      }),
      'empleadosOtros': forms.NumberInput(attrs={
          'class': 'w-full text-center',
      }),
      'empleadosSalario1y2': forms.NumberInput(attrs={
          'class': 'w-full text-center',
      }),
      'empleadosSalario2y4': forms.NumberInput(attrs={
          'class': 'w-full text-center',
      }),
      'empleadosSalariomax4': forms.NumberInput(attrs={
          'class': 'w-full text-center',
      }),
  }

    
SucursalFormSet = forms.inlineformset_factory(
  Pagaduria, SucursalesPagaduria, form=SucursalForm, extra=0, can_delete=True,
)

class PagaduriaUpdateDocumentsForm(forms.ModelForm):
  class Meta:
    model = Pagaduria
    fields = ['convenio', 'formulariovinculacion',
      'tarjetasFirma', 'rut', 'camaraComercio', 'estadosFinancieros',
      'declaracionRenta', 'centrales', 'composicionAccionaria']
    labels = {
      'convenio': 'Convenio',
      'formulariovinculacion': 'Formulario de Vinculación',
      'tarjetasFirma': 'Tarjeta de Firmas',
      'rut': 'RUT',
      'camaraComercio': 'Cámara de Comercio',
      'estadosFinancieros': 'Estados Financieros',
      'declaracionRenta': 'Declaración de Renta',
      'centrales': 'Centrales de Riesgo',
      'composicionAccionaria': 'Composición Accionaria'
    }

class PagaduriaUpdateFinancieraForm(forms.ModelForm):
  class Meta:
    model = Pagaduria
    fields = ['estadoFinanciero', 'scoreFinanciero']
    labels = {
        'estadoFinanciero': 'Estado Financiero',
        'scoreFinanciero': 'Score Financiero'
    }

class PagaduriaUpdateRiesgosForm(forms.ModelForm):
  class Meta:
    model = Pagaduria
    fields = ['estadoRiesgos', 'analisisRiesgos']
    labels = {
        'estadoRiesgos': 'Estado Riesgos',
        'observacionRiesgos': 'Observación Riesgos',
        'analisisRiesgos': 'Analisis Riesgos'
    }

class PagaduriaUpdateComercialForm(forms.ModelForm):
  class Meta:
    model = Pagaduria
    fields = ['estadoComercial', 'scoreComercial']
    labels = {
        'estadoComercial': 'Estado Comercial',
        'scoreComercial': 'Score Comercial'
    }

class ObservacionPagaduriaForm(forms.ModelForm):
  class Meta:
    model = ObservacionesPagaduria
    fields = ['observacion']
    labels = {
      'observacion': 'Observación'
    }
    widgets = {
            'observacion': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Escribe tu observación aquí...'
            }),
        }


class PagaduriaUpdateDatasForm(forms.ModelForm):
  class Meta:
    model = Pagaduria
    fields = [
      'nombre', 'razonSocial', 'sigla', 'nit', 'tipoEmpresa', 'actividadEconomica',
      'departamento', 'ciudad', 'direccion',
      'nombreRepresentante', 'numeroCedulaRepresentante',
      'correoRepresentante', 'telefono', 'cedulaRepresentante',
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
            'departamento': 'Departamento',
            'ciudad': 'Ciudad',
            'direccion': 'Dirección',
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
    widgets = {
            'cedulaRepresentante': forms.FileInput(attrs={
                'class': 'border border-blue-650 rounded-lg p-2 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'
            }),
        }

