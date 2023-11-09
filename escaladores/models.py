from django.db import models

# Create your models here.

class Nuevo_escalador(models.Model):
    nombre= models.CharField(max_length=256)
    fecha_nacimiento= models.DateField(null=True, blank=True)
    nivel= models.CharField(max_length=256)
    preferencia=models.CharField(max_length=250, null=True, blank=True)
