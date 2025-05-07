from django import forms
from .models import CitaProgramada
from account.models import User
from pagadurias.models import Pagaduria

class CitaProgramadaForm(forms.ModelForm):
  class Meta:
    model = CitaProgramada
    fields = ['pagaduria', 'asesor', 'fecha', 'hora', 'notas']
    widgets = {
        'fecha': forms.DateInput(attrs={'type': 'date'}),
        'hora': forms.TimeInput(attrs={'type': 'time'}),
        'notas': forms.Textarea(attrs={
          'rows': '6',
          'placeholder': 'Opcional: En caso que requiera registrar una nota.'
        })
    }
    
  def __init__(self, *args, **kwargs):
    user = kwargs.pop('user', None)
    super().__init__(*args, **kwargs)
    
    if user:
      self.fields['asesor'].queryset = User.objects.filter(id=user.id)
      self.fields['asesor'].initial = user
      
      self.fields['pagaduria'].queryset = Pagaduria.objects.filter(asesores=user)

class CitaProgramadaCloseForm(forms.ModelForm):
  class Meta:
    model = CitaProgramada
    fields = ['resultado']
    widgets = {
      'resultado': forms.Textarea(attrs={
        'class': 'w-full p-3 shadow-md rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none',
        'rows': '5',
        'placeholder': 'Ingrese reporte...',
        })
    }
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['resultado'].required = True