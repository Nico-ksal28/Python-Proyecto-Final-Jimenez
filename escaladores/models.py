from django.db import models

# Create your models here.

class Nuevo_escalador(models.Model):
    nombre= models.CharField(max_length=256)
    fecha_nacimiento= models.DateField(null=True, blank=True)
    nivel= models.CharField(max_length=256)
    preferencia=models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre}, {self.nivel}, {self.preferencia}"
    
class nueva_ruta(models.Model):
    nombre_ruta= models.CharField(max_length=256)
    grado= models.CharField(max_length=256)
    nombre_parque= models.CharField(max_length=256)

    def __str__(self):
        return f"{self.nombre_ruta}, {self.grado}, {self.nombre_parque}"
    

class nuevo_bloque(models.Model):
    nombre_bloque= models.CharField(max_length=256)
    grado= models.CharField(max_length=256)
    nombre_parque= models.CharField(max_length=256)

    def __str__(self):
        return f"{self.nombre_bloque}, {self.grado}, {self.nombre_parque}"
