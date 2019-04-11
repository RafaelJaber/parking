from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import (
    Person, 
    Vehicle, 
    MoveRotary, 
    Monthly, 
    MoveMonthly
)
from .forms import (
    PersonForm,
    VehicleForm
)

def home(request):
    context = {'mensagem': 'Olá Jáber'}
    return render(request, 'core/index.html', context)


def listPerson(request):
    person = Person.objects.all()
    form = PersonForm()
    data = {'persons': person,'form': form}
    return render(request, 
        'core/list_person.html', 
        data
    )
def personRegister(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_list_person')


def listVehicles(request):
    vehicles = Vehicle.objects.all()
    form = VehicleForm()
    data = {'vehicles': vehicles, 'form': form}
    return render(request, 
        'core/list_vehicles.html', 
        data
    )
def vehicleRegister(request):
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_list_vehicles')


def listMovRotarys(request):
    movRotarys = MoveRotary.objects.all()
    return render(request, 
        'core/list_movrotary.html', 
        {'movRotarys': movRotarys}
    )

def listMovMonthly(request):
    movMonthly = Monthly.objects.all()
    return render(request, 
        'core/list_movmonthly.html', 
        {'movMonthlys': movMonthly}
    )

def listMonthly(request):
    monthly = MoveMonthly.objects.all()
    return render(request, 
        'core/list_monthly.html', 
        {'monthlys': monthly}
    )