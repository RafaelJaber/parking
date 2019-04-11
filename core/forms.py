from django.forms import ModelForm
from .models import (
    Person,
    Vehicle,
)


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'