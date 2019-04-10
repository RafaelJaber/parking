from django.contrib import admin
from .models import (
    Brand, 
    Vehicle, 
    Person, 
    Parameters, 
    MoveRotary
)

admin.site.register(Brand)
admin.site.register(Vehicle)
admin.site.register(Person)
admin.site.register(Parameters)
admin.site.register(MoveRotary)
