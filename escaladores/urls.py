from django.contrib import admin
from django.urls import path

#URLs de 

from escaladores.views import *


urlpatterns = [
    
    #URLs CLASES 
    #URLs ESCALADORES
    path ("informacion_escalada/", Nuevo_escaladorListView.as_view(), name="informacion_escalada"),
    path ("informacion_escalada/<int:pk>/", Nuevo_escaladorDetailView.as_view(), name="ver_escalador"),
    path("registro_escalador/",Nuevo_escaladorCreateView.as_view(), name= "registrar_escalador"),
    path("editar_escalador/<int:pk>/", Nuevo_escaladorUpdateView.as_view(), name = "editar_escalador"),
    path("eliminar_escalador/<int:pk>/",Nuevo_escaladorDeleteView.as_view(), name="eliminar_escalador"),

    #URLs RUTAS
    path ("rutas/", nueva_rutaListView.as_view(), name="informacion_vias"),
    path ("rutas/<int:pk>/", nueva_rutaDetailView.as_view(), name="ver_ruta"),
    path("registro_ruta/",nueva_rutaCreateView.as_view(), name= "registrar_ruta"),
    path("editar_ruta/<int:pk>/", nueva_rutaUpdateView.as_view(), name = "editar_ruta"),
    path("eliminar_ruta/<int:pk>/",nueva_rutaDeleteView.as_view(), name="eliminar_ruta"),

    #URLs BLOQUES
    path ("bloques/", nuevo_bloqueListView.as_view(), name="informacion_bloques"),
    path ("bloques/<int:pk>/", nuevo_bloqueDetailView.as_view(), name="ver_bloque"),
    path("registro_bloque/",nuevo_bloqueCreateView.as_view(), name= "registrar_bloque"),
    path("editar_bloque/<int:pk>/", nuevo_bloqueUpdateView.as_view(), name = "editar_bloque"),
    path("eliminar_bloque/<int:pk>/",nuevo_bloqueDeleteView.as_view(), name="eliminar_bloque"),
]
