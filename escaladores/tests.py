from django.test import TestCase
from escaladores.models import *


class nueva_rutaTests(TestCase):
   """En esta clase van todas las pruebas del modelo nueva_ruta."""
   def test_nueva_ruta(self):
    Nueva_ruta = nueva_ruta(nombre_ruta="Titulo", grado="1000", nombre_parque="titulo")
    Nueva_ruta.save()

    self.assertEqual(nueva_ruta.objects.count(), 1)
    self.assertEqual(Nueva_ruta.nombre_ruta, "Titulo")
    self.assertEqual(Nueva_ruta.grado, "1000")
    self.assertEqual(Nueva_ruta.nombre_parque, "titulo")

   def test_nueva_ruta_str(self):
    Nueva_ruta = nueva_ruta(nombre_ruta="Titulo", grado="1000", nombre_parque="titulo")
    Nueva_ruta.save()

    self.assertEqual(Nueva_ruta.__str__(), "Titulo, 1000, titulo")