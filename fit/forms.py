#from django import Modelform
from django import forms
from fit.models import *


class calforms(forms.ModelForm):
    class Meta:
        model = CalculadoraForms
        fields = '__all__'

    widgets = {
            'genero': forms.RadioSelect(),
            'objetivo': forms.RadioSelect(),
            'atividade': forms.RadioSelect(),
        }