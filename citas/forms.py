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