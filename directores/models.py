from django.db import models
from django.urls import reverse

# Create your models here.
class Director(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    date_of_birth = models.DateField(null = True, blank=True)
    date_of_death = models.DateField(null = True, blank=True)
    
    def __str__(self):
        return '%s, %s' % (self.nombre,self.apellido)
    
class Peliculas(models.Model):
    pelicula = models.CharField(max_length=50)
    descripcion = models.TextField()
    autor = models.ForeignKey('Director', on_delete=models.SET_NULL, null = True)
    estreno = models.DateField(null = True, blank=True)
    
    def __str__(self):
        return self.pelicula
    
    

    
