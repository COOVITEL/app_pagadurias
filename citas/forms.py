from django import forms
from .models import CitaProgramada

class CitaProgramadaForm(forms.ModelForm):
  class Meta:
    model = CitaProgramada
    fields = ['pagaduria', 'asesor', 'fecha', 'hora', 'notas']
    widgets = {
        'fecha': forms.DateInput(attrs={'type': 'date'}),
        'hora': forms.TimeInput(attrs={'type': 'time'}),
    }

class CitaProgramadaCloseForm(forms.ModelForm):
  class Meta:
    model = CitaProgramada
    fields = ['resultado']
    widgets = {
      'resultado': forms.Textarea(attrs={
        'class': 'w-full p-3 shadow-md rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none',
        'rows': '5',
        'placeholder': 'Ingrese reporte...'
        })
    }