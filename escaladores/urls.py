from django.contrib import admin
from django.urls import path

#URLs de 

from escaladores.views import informacion_escalada
from escaladores.views import informacion_vias
from escaladores.views import informacion_bloques


urlpatterns = [
    path ("informacion_escalada/", informacion_escalada, name="informacion_escalada"),
    path ("rutas/", informacion_vias, name="informacion_vias"),
    path ("bloques/", informacion_bloques, name="informacion_bloques"),
]