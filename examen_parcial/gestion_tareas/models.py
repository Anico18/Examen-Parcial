from django.db import models

# Create your models here.
class usuariosDjango(models.Model):
    id = models.IntegerField(primary_key='true', default='')
    nombre = models.CharField(max_length=64, default='')
    apellido = models.CharField(max_length=64, default='')
    tarea = models.CharField(max_length=128, default='')
    fecha = models.DateField(max_length=64, default='')