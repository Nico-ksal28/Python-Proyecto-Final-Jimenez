from django.contrib import admin
from django.urls import path

#URLs de 

from escaladores.views import informacion_escalada


urlpatterns = [
    path ("informacion_escalada/", informacion_escalada)

]