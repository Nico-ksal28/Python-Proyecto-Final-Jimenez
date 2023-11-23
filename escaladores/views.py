from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q

from escaladores.forms import *
from escaladores.models import *

# Create your views here.

#Vistas de Escaladores definidas por clase 

#Escaladores
class Nuevo_escaladorListView(ListView):
    model = Nuevo_escalador
    template_name= 'escaladores/informacion_escalada.html'

class Nuevo_escaladorCreateView(CreateView):
    model = Nuevo_escalador
    fields = ('nombre', 'nivel', 'preferencia')
    success_url = reverse_lazy ('informacion_escalada')

class Nuevo_escaladorDetailView(DetailView):
    model= Nuevo_escalador
    success_url= reverse_lazy('informacion_escalada')

class Nuevo_escaladorUpdateView(UpdateView):
    model = Nuevo_escalador
    fields = ('nombre', 'nivel', 'preferencia')
    success_url = reverse_lazy ('informacion_escalada')

class Nuevo_escaladorDeleteView(DeleteView):
    model= Nuevo_escalador
    success_url= reverse_lazy('informacion_escalada')

#Vias
class nueva_rutaListView(ListView):
    model = nueva_ruta
    template_name= 'escaladores/nueva_ruta.html'

class nueva_rutaCreateView(CreateView):
    model = nueva_ruta
    fields = ('nombre_ruta', 'grado', 'nombre_parque')
    success_url = reverse_lazy ('infromacion_vias')

class nueva_rutaDetailView(DetailView):
    model= nueva_ruta
    succes_url = reverse_lazy('informacion_vias')

class nueva_rutaUpdateView(UpdateView):
    model= nueva_ruta
    fields = ('nombre_ruta', 'grado', 'nombre_parque')
    success_url= reverse_lazy('informacion_vias')

class nueva_rutaDeleteView(DeleteView):
    model= nueva_ruta
    success_url= reverse_lazy('informacion_vias')

#Bloques
class nuevo_bloqueListView(ListView):
    model = nuevo_bloque
    template_name= 'escaladores/nuevo_bloque.html'

class nuevo_bloqueCreateView(CreateView):
    model = nuevo_bloque
    fields = ('nombre_bloque', 'grado', 'nombre_parque')
    success_url = reverse_lazy ('informacion_bloques')

class nuevo_bloqueDetailView(DetailView):
    model= nuevo_bloque
    succes_url = reverse_lazy('informacion_bloques')

class nuevo_bloqueUpdateView(UpdateView):
    model= nuevo_bloque
    fields = ('nombre_bloque', 'grado', 'nombre_parque')
    success_url= reverse_lazy('informacion_bloques')

class nuevo_bloqueDeleteView(DeleteView):
    model= nuevo_bloque
    success_url= reverse_lazy('informacion_bloques')