from django.contrib import admin
from django.urls import path

from escaladores.views import registrar_escaladores

urlpatterns = [
    path ("lista_escaladores/", registrar_escaladores),
]