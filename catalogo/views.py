from django.shortcuts import render, redirect
from .models import Vehiculo, Factura
from .forms import VehiculoForm

# Create your views here.
def listaVehiculos(request):
    vehiculo = Vehiculo.objects.all()
    return render(request, 'listaVehiculos.html',{
        'vehiculos': vehiculo,
    })
    
def crearVehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            nuevoVehiculo = form.save(commit=False)
            nuevoVehiculo.save()
            print(nuevoVehiculo)
            return redirect('listaVehiculos.html',
                {'form': form})
    else:
        form = VehiculoForm()
    return render(request, 'crearVehiculo.html', {'form': form})