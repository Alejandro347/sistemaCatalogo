from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vehiculo(models.Model):
    modelo = models.CharField(max_length=50, blank=False)
    categoria = models.CharField(max_length=50, blank=False)
    estado = models.CharField(max_length=50, blank=False)
    disponibilidad = models.CharField(max_length=50, blank=False)
    descripcion = models.TextField(max_length=200, blank=False)
    transmision = models.CharField(max_length=50, blank=False)
    kilometraje = models.IntegerField(blank=False, default=0)
    
class Factura(models.Model):
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    fechaInicio = models.DateField(blank=False)
    fechaFin = models.DateField(blank=False)
    auto = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)