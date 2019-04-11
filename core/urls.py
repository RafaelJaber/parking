from django.urls import path
from .views import (
    home, 
    listPerson, 
    listVehicles, 
    listMovRotarys, 
    listMovMonthly, 
    listMonthly,
    personRegister,
    vehicleRegister,
)


urlpatterns = [
    path('', home, name='core_home'),
    path('persons/', listPerson, name='core_list_person'),
    path('persons_register/', personRegister, name='core_person_register'),
    path('vehicles/', listVehicles, name='core_list_vehicles'),
    path('vehicles_register/', vehicleRegister, name='core_vehicles_register'),
    path('rotarys/', listMovRotarys, name='core_list_mov_rotarys'),
    path('mov-monthly/', listMovMonthly, name='core_list_mov_monthly'),
    path('monthly/', listMonthly, name='core_list_monthly'),
]