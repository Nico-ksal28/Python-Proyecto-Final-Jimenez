from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q

from escaladores.forms import *
from escaladores.models import *

# Create your views here.

"""def informacion_escalada(request):
    contexto = {
        'nuevo_escalador': Nuevo_escalador.objects.all,
    }
    http_response = render(
        request=request,
        template_name= 'escaladores/informacion_escalada.html',
        context=contexto,
    )
    return http_response"""

"""def registrar_ruta(request):
   if request.method == "POST":
       formulario = nueva_rutaFormulario(request.POST)
       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario 
           nombre_ruta = data['nombre_ruta']
           grado = data['grado']
           nombre_parque = data['nombre_parque']
           ruta = nueva_ruta(nombre_ruta=nombre_ruta, grado=grado, nombre_parque=nombre_parque)  # lo crean solo en RAM
           ruta.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('informacion_vias')  # estudios/cursos/
           return redirect(url_exitosa)
   else:  # GET
       formulario = nueva_rutaFormulario()
   http_response = render(
       request=request,
       template_name='escaladores/registrar_ruta.html',
       context={'formulario': formulario}
   )
   return http_response

def registrar_bloque(request):
   if request.method == "POST":
       formulario = nuevo_bloqueFormulario(request.POST)
       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario 
           nombre_bloque = data['nombre_bloque']
           grado = data['grado']
           nombre_parque = data['nombre_parque']
           bloque = nuevo_bloque(nombre_bloque=nombre_bloque, grado=grado, nombre_parque=nombre_parque)  # lo crean solo en RAM
           bloque.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('informacion_bloques')  
           return redirect(url_exitosa)
   else:  # GET
       formulario = nuevo_bloqueFormulario()
   http_response = render(
       request=request,
       template_name='escaladores/registrar_bloque.html',
       context={'formulario': formulario}
   )
   return http_response

def buscar_rutas(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        # Filtro simple
        # rutas = nueva_ruta.objects.filter(grado__contains=busqueda)
        # Ejemplo filtro avanzado

        ruta = nueva_ruta.objects.filter(
            Q(nombre_ruta__icontains=busqueda) | Q(grado__contains=busqueda) | Q(nombre_parque__contains=busqueda)
            )

        contexto = {
            "nueva_ruta": ruta,
        }
        http_response = render(
            request=request,
            template_name='escaladores/nueva_ruta.html',
            context=contexto,
        )
        return http_response
    
def borrar_ruta(request, id):
    
    ruta= nueva_ruta.objects.get(id=id)
    if request.method == "POST":
        ruta.delete()
        url_exitosa = reverse('informacion_vias')
        return redirect(url_exitosa)

def editar_ruta(request, id):

    ruta = nueva_ruta.objects.get(id=id)
    if request.method == "POST":
        formulario = nueva_rutaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            ruta.nombre_ruta = data['nombre_ruta']
            ruta.grado = data['grado']
            ruta.nombre_parque = data['nombre_parque']
            ruta.save()

            url_exitosa = reverse('informacion_vias')
        return redirect(url_exitosa)
    else:
        inicial = {
            'nombre_ruta': ruta.nombre_ruta,
            'grado': ruta.grado,
            'nombre_parque': ruta.nombre_parque,
        }
        formulario= nueva_rutaFormulario(initial=inicial)
    return render(
        request=request,
        template_name='escaladores/registrar_ruta.html',
       context={'formulario': formulario}
    )"""

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

#vias
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

#bloques
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