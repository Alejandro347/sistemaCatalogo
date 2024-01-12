from django.forms import ModelForm
from .models import Vehiculo
from django import forms
class VehiculoForm(ModelForm):
    TRANSMISION_CHOICES = (
        ('Automatico', 'Automatico'),
        ('Manual', 'Manual'),
    )
    
    CATEGORIA_CHOICES = (
        ('Sedan', 'Sedan'),
        ('Hatchback', 'Hatchback'),
        ('SUV', 'SUV'),
        ('Minivan', 'Minivan'),
        ('Pickup', 'Pickup'),
        ('Deportivo', 'Deportivo'),
    )
    
    DISPONIBILIDAD_CHOICES = (
        ('Renta','Renta'),
        ('Venta','Venta'),
    )
    
    ESTADO_CHOICES = (
        ('Nuevo','Nuevo'),
        ('Usado','Usado'),
    )
    
    marca = forms.CharField(max_length=50, required=True, label='Marca')
    modelo = forms.CharField(max_length=50, required=True, label='Modelo')
    categoria = forms.ChoiceField(choices=CATEGORIA_CHOICES, required=True, label='Categoria')
    estado = forms.ChoiceField(choices=ESTADO_CHOICES, required=True, label='Estado')
    disponibilidad = forms.ChoiceField(choices=DISPONIBILIDAD_CHOICES, required=True, label='Disponibilidad')
    descripcion = forms.CharField(max_length=200, required=True, label='Descripcion')
    transmision = forms.ChoiceField(choices=TRANSMISION_CHOICES, required=True, label='Transmision')
    kilometraje = forms.IntegerField(required=True, label='Kilometraje')
    
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'categoria', 'estado', 'disponibilidad', 'descripcion', 'transmision', 'kilometraje']