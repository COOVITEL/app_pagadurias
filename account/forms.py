from django import forms
from .models import User

class UpdateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['cedula', 'area', 'checkForTI']