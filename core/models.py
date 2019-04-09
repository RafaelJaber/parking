from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)


class Brand(models.Model):
    name= models.CharField(max_length=50)


class Vehicle(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    board = models.CharField(max_length=7)
    color = models.CharField(max_length=15)
    note = models.TextField()
