from django.db import models
import math

class Person(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    


class Brand(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Vehicle(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    board = models.CharField(max_length=7)
    ouwner = models.ForeignKey(Person, on_delete=models.CASCADE)
    color = models.CharField(max_length=15)
    note = models.TextField()

    def __str__(self): 
        return self.brand.name + ' - ' + self.board


class Parameters(models.Model):
    value_hour = models.DecimalField(max_digits=5, decimal_places=2)
    value_month = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return "Parametros Gerais"


class MoveRotary(models.Model):
    checkin = models.DateTimeField(auto_now=False)
    checkout = models.DateTimeField(auto_now=False, null=True, blank=True)
    value_our = models.DecimalField(max_digits=5, decimal_places=2)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)

    def total_hours(self):
        return math.ceil((self.checkout - self.checkin).total_seconds() / 3600)

    def total(self):
            return self.value_our * self.total_hours()

    def __str__(self):
        return self.vehicle.board


class MoveMonthly(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start = models.DateField()
    value_month = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.vehicle) + ' - ' + str(self.start)
    

class Monthly(models.Model):
    moveMonthly = models.ForeignKey(MoveMonthly, on_delete=models.CASCADE)
    date_paid = models.DateField()
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.moveMonthly) + ' - ' + str(self.total)
    