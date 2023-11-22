from django.contrib import admin
from django.urls import path

#URLs de 

from escaladores.views import *


urlpatterns = [
    
    path ("registro_ruta/",registrar_ruta, name="registrar_ruta"),
    path ("registro_bloque/",registrar_bloque, name="registrar_bloque"),
    path ("registro_escalador/",registrar_escalador, name="registrar_escalador"),
    path("buscar_rutas/", buscar_rutas, name="buscar_rutas"),
    path ("borrar_ruta/<int:id>/",borrar_ruta, name="borrar_ruta"),
    path ("editar_ruta/<int:id>/",editar_ruta, name="editar_ruta"),
    #URLs CLASES 
    path ("informacion_escalada/", Nuevo_escaladorListView.as_view(), name="informacion_escalada"),
    path ("rutas/", nueva_rutaListView.as_view(), name="informacion_vias"),
    path ("bloques/", nuevo_bloqueListView.as_view(), name="informacion_bloques"),
]
