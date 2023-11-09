from django.shortcuts import render

from escaladores.models import Nuevo_escalador

# Create your views here.

def registrar_escaladores(request):
    contexto = {
        'pagina_escalada': Nuevo_escalador.objects.all
    }
    http_response = render(
        request=request,
        template_name= 'escaladores/registro_escalador.html',
        context=contexto,
    )
    return http_response