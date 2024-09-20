from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='images/')
    # price = models.IntegerField()
    # discount_price = models.IntegerField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to='books/')
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

class Car(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    color = models.CharField(max_length=255)
    vin = models.IntegerField()
    transmission_type = models.CharField(max_length=255)
    mileage = models.DecimalField(max_digits=9, decimal_places=2)
    fuel_type = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)

    def __str__(self):
        return self.name