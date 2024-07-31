from django.db import models

# Create your models here.

class Person(models.Model):
    fullname = models.CharField(max_length=250)
    nickname = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)

class OrderDetail(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)