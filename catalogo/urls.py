from django.urls import path, include
from . import views

urlpatterns = [
    path('listaVehiculos/', views.listaVehiculos, name='listaVehiculos'),
    path('crearVehiculo/', views.crearVehiculo, name='crearVehiculo'),
]
