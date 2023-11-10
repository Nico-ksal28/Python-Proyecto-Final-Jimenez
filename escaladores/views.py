from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q



from escaladores.forms import nueva_rutaFormulario, nuevo_bloqueFormulario, Nuevo_escaladorFormulario
from escaladores.models import *

# Create your views here.

def informacion_escalada(request):
    contexto = {
        'nuevo_escalador': Nuevo_escalador.objects.all,
    }
    http_response = render(
        request=request,
        template_name= 'escaladores/informacion_escalada.html',
        context=contexto,
    )
    return http_response

def informacion_vias(request):
    contexto = {
        'nueva_ruta': nueva_ruta.objects.all,
    }
    http_response = render(
        request=request,
        template_name= 'escaladores/nueva_ruta.html',
        context=contexto,
    )
    return http_response

def informacion_bloques(request):
    contexto = {
        'nuevo_bloque': nuevo_bloque.objects.all,
    }
    http_response = render(
        request=request,
        template_name= 'escaladores/nuevo_bloque.html',
        context=contexto,
    )
    return http_response

def registrar_ruta(request):
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

def registrar_escalador(request):
   if request.method == "POST":
       formulario = Nuevo_escaladorFormulario(request.POST)
       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario 
           nombre= data['nombre']
           nivel = data['nivel']
           preferencia = data['preferencia']
           escalador = Nuevo_escalador(nombre=nombre, nivel=nivel, preferencia=preferencia)  # lo crean solo en RAM
           escalador.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('informacion_escalada')  
           return redirect(url_exitosa)
   else:  # GET
       formulario = Nuevo_escaladorFormulario()
   http_response = render(
       request=request,
       template_name='escaladores/registrar_escalador.html',
       context={'formulario': formulario}
   )
   return http_response

def buscar_rutas(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        # Filtro simple
        rutas = nueva_ruta.objects.filter(grado__contains=busqueda)
        # Ejemplo filtro avanzado
        #rutas = nueva_ruta.objects.filter(Q(nombre_ruta__icontains=busqueda) | Q(grado__contains=busqueda)| Q(nombre_parque__contains=busqueda))

        contexto = {
            "rutas": rutas,
        }
        http_response = render(
            request=request,
            template_name='escaladores/nueva_ruta.html',
            context=contexto,
        )
        return http_response
