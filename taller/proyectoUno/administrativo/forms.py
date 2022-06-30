from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Edificio, \
        Departamento

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'direccion': _('Ingrese la dirección por favor'),
            'ciudad': _('Ingrese ciudad por favor'),
            'tipo': _('Ingrese tipo por favor'),
        }


    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']
        if valor.startswith('L'):
            raise forms.ValidationError("Ingrese una ciudad correcta")
        return valor



class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre_prop', 'costo_dep', 'num_cuartos','edificio']


    def clean_costo_dep(self):
        valor = self.cleaned_data['costo_dep']
        

        if valor > 100000:
            raise forms.ValidationError("Ingrese un valor menor a $100mil")
        return valor


    def clean_num_cuartos(self):
        valor = self.cleaned_data['num_cuartos']
        
        if valor == 0 or valor > 7:
            raise forms.ValidationError("Ingrese un número entre 1 y 6")
        return valor


    def clean_nombre(self):
        valor = self.cleaned_data['nombre_prop']
        num_palabras = len(valor.split())

        if num_palabras < 3:
            raise forms.ValidationError("Ingrese los nombres completos por favor")
        return valor


class DepartamentoEdificioForm(ModelForm):

    def __init__(self, Edificio, *args, **kwargs):
        super(DepartamentoEdificioForm, self).__init__(*args, **kwargs)
        self.initial['edificio'] = Edificio
        self.fields["edificio"].widget = forms.widgets.HiddenInput()
        print(Edificio)

    class Meta:
        model = Departamento
        fields = ['nombre_prop', 'costo_dep', 'num_cuartos','edificio']
