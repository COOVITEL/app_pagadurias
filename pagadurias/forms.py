from django.forms import ModelForm
from .models import Pagaduria

class PagaduriaForm(ModelForm):
  class Meta:
    model = Pagaduria
    fields = [
      'nombre', 'razonSocial', 'sigla', 'nit', 'tipoEmpresa',
      'actividadEconomica', 'estado', 'pais', 'departamento',
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