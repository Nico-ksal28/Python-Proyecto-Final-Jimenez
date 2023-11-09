from django.contrib import admin
from django.urls import path

from escaladores.views import registro_escalada

urlpatterns = [
    path ("registro_escalada/", registro_escalada),
]