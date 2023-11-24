from django.shortcuts import render, redirect
from django import forms 
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from escaladores.forms import *
from escaladores.models import *

# Create your views here.

#Vistas de about

def about(request):
    contexto = {
    }
    http_response = render(
        request=request,
        template_name='about.html',
        context=contexto,
    )
    return http_response

def contacto(request):
    contexto = {
    }
    http_response = render(
        request=request,
        template_name='contacto.html',
        context=contexto,
    )
    return http_response

#Escaladores

class Nuevo_escaladorListView(LoginRequiredMixin, ListView):
    model = Nuevo_escalador
    template_name= 'escaladores/informacion_escalada.html'

class Nuevo_escaladorCreateView(LoginRequiredMixin, CreateView):
    model = Nuevo_escalador
    fields = ('nombre', 'nivel', 'preferencia')
    success_url = reverse_lazy ('informacion_escalada')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(creador=self.request.user)
        return super().form_valid(form)

class Nuevo_escaladorDetailView(LoginRequiredMixin, DetailView):
    model= Nuevo_escalador
    success_url= reverse_lazy('informacion_escalada')

class Nuevo_escaladorUpdateView(LoginRequiredMixin, UpdateView):
    model = Nuevo_escalador
    fields = ('nombre', 'nivel', 'preferencia')
    success_url = reverse_lazy ('informacion_escalada')

class Nuevo_escaladorDeleteView(LoginRequiredMixin, DeleteView):
    model= Nuevo_escalador
    success_url= reverse_lazy('informacion_escalada')

#Vias
class nueva_rutaListView(ListView):
    model = nueva_ruta
    template_name= 'escaladores/nueva_ruta.html'

class nueva_rutaCreateView(LoginRequiredMixin, CreateView):
    model = nueva_ruta
    fields = ('nombre_ruta', 'grado', 'nombre_parque')
    success_url = reverse_lazy ('informacion_vias')

    def form_valid(self, form):
        #If the form is valid, save the associated model.
        self.object = form.save(creador=self.request.user)
        return super().form_valid(form)

class nueva_rutaDetailView(DetailView):
    model= nueva_ruta
    succes_url = reverse_lazy('informacion_vias')

class nueva_rutaUpdateView(LoginRequiredMixin, UpdateView):
    model= nueva_ruta
    fields = ('nombre_ruta', 'grado', 'nombre_parque')
    success_url= reverse_lazy('informacion_vias')

class nueva_rutaDeleteView(LoginRequiredMixin, DeleteView):
    model= nueva_ruta
    success_url= reverse_lazy('informacion_vias')

#Bloques
class nuevo_bloqueListView(ListView):
    model = nuevo_bloque
    template_name= 'escaladores/nuevo_bloque.html'

class nuevo_bloqueCreateView(LoginRequiredMixin, CreateView):
    model = nuevo_bloque
    fields = ('nombre_bloque', 'grado', 'nombre_parque')
    success_url = reverse_lazy ('informacion_bloques')

class nuevo_bloqueDetailView(DetailView):
    model= nuevo_bloque
    succes_url = reverse_lazy('informacion_bloques')

class nuevo_bloqueUpdateView(LoginRequiredMixin, UpdateView):
    model= nuevo_bloque
    fields = ('nombre_bloque', 'grado', 'nombre_parque')
    success_url= reverse_lazy('informacion_bloques')

class nuevo_bloqueDeleteView(LoginRequiredMixin, DeleteView):
    model= nuevo_bloque
    success_url= reverse_lazy('informacion_bloques')