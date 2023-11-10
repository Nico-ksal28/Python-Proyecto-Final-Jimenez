from django.contrib import admin
from django.urls import path

#URLs de 

from escaladores.views import informacion_escalada
from escaladores.views import informacion_vias
from escaladores.views import informacion_bloques
from escaladores.views import (
    registrar_ruta, registrar_bloque, registrar_escalador, buscar_rutas
)



urlpatterns = [
    path ("informacion_escalada/", informacion_escalada, name="informacion_escalada"),
    path ("rutas/", informacion_vias, name="informacion_vias"),
    path ("bloques/", informacion_bloques, name="informacion_bloques"),
    path ("registro_ruta/",registrar_ruta, name="registrar_ruta"),
    path ("registro_bloque/",registrar_bloque, name="registrar_bloque"),
    path ("registro_escalador/",registrar_escalador, name="registrar_escalador"),
    path("buscar-rutas/", buscar_rutas, name="buscar_rutas"),
]