from django.contrib import messages
from django.http.response import HttpResponseRedirect
from .forms import VehicleForm
from django.shortcuts import render
from .models import Vehicle

# Create your views here.

def vehicle(request):
    vehicles = Vehicle.objects.all()
    context = {'booking' : 'active', 'vehicle' : 'active', 'vehicle_show' : vehicles}
    return render(request, 'vehicles/vehicle.html', context)

def add_vehicle(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = VehicleForm(request.POST)
            if form.is_valid():
                vehicle = form.save()
                name = vehicle.name
                messages.success(request, name + '.. New Vehicle has been added.')
                return HttpResponseRedirect('/booking/vehicle/', {'vehicle' : 'active'})

        else:
            form = VehicleForm()

    context = { 'vehicle' : 'active', 'fm' : VehicleForm}
    return render(request, 'vehicles/add_vehicle.html', context)


def delete_vehicle(request, vehicle_id):
    vehicle = Vehicle.objects.get(id = vehicle_id)
    vehicle.delete()
    messages.success(request, 'Vehicle Successfully Deleted')
    return HttpResponseRedirect('/booking/vehicle/', {'vehicle' : 'active'})

def vehicle_info(request, vehicle_name):
    vehicle_more = Vehicle.objects.get(name=vehicle_name)
    context = {'booking' : 'active', 'vehicle' : 'active', 'vehicle_more' : vehicle_more}
    return render(request, 'vehicles/vehicle_info.html', context)
