from django.shortcuts import render
from .models import Vehiculo
from .forms import VehiculoForm

# Create your views here.
def crearVehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            nuevoVehiculo = form.save(commit=False)
            nuevoVehiculo.save()
            return render(
                request,'catalogo/crearVehiculo.html/',
                {'form': form})
    else:
        form = VehiculoForm()
    return render(request, 'catalogo/crearVehiculo.html/', {'form': form})