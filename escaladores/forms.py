from django import forms

class nueva_rutaFormulario(forms.Form):
    nombre_ruta = forms.CharField(required=True, max_length=256)
    grado = forms.CharField(required=True, max_length=256)
    nombre_parque = forms.CharField(required=True, max_length=256)

class nuevo_bloqueFormulario(forms.Form):
    nombre_bloque = forms.CharField(required=True, max_length=256)
    grado = forms.CharField(required=True, max_length=256)
    nombre_parque = forms.CharField(required=True, max_length=256)

class Nuevo_escaladorFormulario(forms.Form):
    nombre = forms.CharField( max_length=256)
    nivel = forms.CharField(required=True, max_length=256)
    preferencia = forms.CharField(required=True, max_length=256)
