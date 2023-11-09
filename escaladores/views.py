from django.shortcuts import render

from escaladores.models import Nuevo_escalador
from escaladores.models import nueva_ruta
from escaladores.models import nuevo_bloque

# Create your views here.

def registrar_escaladores(request):
    contexto = {
        'nuevo_escalador': Nuevo_escalador.objects.all,
        'nueva_ruta': nueva_ruta.objects.all,
        'nuevo_bloque': nuevo_bloque.objects.all,
    }
    http_response = render(
        request=request,
        template_name= 'escaladores/registro_escalador.html',
        context=contexto,
    )
    return http_response
