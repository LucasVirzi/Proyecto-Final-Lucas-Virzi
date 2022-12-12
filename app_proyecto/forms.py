from django import forms
from app_proyecto.models import Familiar

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100,
          widget=forms.TextInput(attrs={'placeholder': 'Buscar...'}))


class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']