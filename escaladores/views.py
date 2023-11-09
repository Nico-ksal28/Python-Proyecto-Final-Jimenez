from django.shortcuts import render

from escaladores.models import Nuevo_escalador
from escaladores.models import nueva_ruta
from escaladores.models import nuevo_bloque

# Create your views here.

def informacion_escalada(request):
    contexto = {
        'nuevo_escalador': Nuevo_escalador.objects.all,
        'nueva_ruta': nueva_ruta.objects.all,
        'nuevo_bloque': nuevo_bloque.objects.all,
    }
    http_response = render(
        request=request,
        template_name= 'escaladores/informacion_escalada.html',
        context=contexto,
    )
    return http_response
