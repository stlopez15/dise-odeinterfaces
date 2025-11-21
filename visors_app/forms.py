from django import forms
from .models import InterfaceAR

class InterfaceForm(forms.ModelForm):
    class Meta:
        model = InterfaceAR
        fields = ['nombre', 'imagen', 'marcador']
