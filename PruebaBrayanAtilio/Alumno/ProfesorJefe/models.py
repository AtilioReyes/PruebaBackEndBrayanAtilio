from django.db import models

class ProfJefe(models.Model):
    nombre = models.CharField(max_length=40,verbose_name="nombre")
    edad = models.CharField(max_length=2,verbose_name="edad")
    asignatura = models.CharField( max_length=30,verbose_name="asignatura")
    rut = models.CharField(max_length=12,verbose_name="rut")
    correo = models.CharField(max_length=100,verbose_name="correo")
    horario = models.CharField(max_length= 40,verbose_name="horario")
    


# Create your models here.
