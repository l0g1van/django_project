from django.db import models
from django.core.validators import RegexValidator


class Users(models.Model):

    name = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class City(models.Model):

    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    continent = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=75)


class Customer(models.Model):

    city = models.ForeignKey(City, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    address = models.CharField(max_length=75)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. "
                                         "Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)


class Retailer(models.Model):
    name = models.CharField(max_length=50)
    city = models.OneToOneField(City, on_delete=models.CASCADE, default=1)
