from django import forms
from app_proyecto.models import (Familiar, Mascota, Auto)

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100,
          widget=forms.TextInput(attrs={'placeholder': 'Buscar...'}))


class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']

class MascotaForm(forms.ModelForm):
  class Meta:
    model = Mascota
    fields = ['nombre', 'dueño', 'raza']

class AutoForm(forms.ModelForm):
  class Meta:
    model = Auto
    fields = ['marca', 'dueño', 'numero_patente']

