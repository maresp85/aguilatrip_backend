from django.db import models
from django.contrib.auth.models import User

import datetime

class Country(models.Model):
    name = models.CharField(max_length=80, null=False)


class City(models.Model):
    name = models.CharField(max_length=80, null=False)
    country = models.ForeignKey(Country, null=False, on_delete=models.PROTECT)


class Car(models.Model):
    plate = models.CharField(max_length=7, null=False)
    brand = models.CharField(max_length=30, null=False)


class Status_trip(models.Model):
    name = models.CharField(max_length=20, null=False)


class Check_code(models.Model):
    code = models.AutoField(primary_key=True)


class Trip(models.Model):
    passenger = models.ForeignKey(User, null=False, on_delete=models.PROTECT, related_name="passenger")
    driver = models.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name="driver")
    car = models.ForeignKey(Car, null=True, on_delete=models.PROTECT)
    status = models.ForeignKey(Status_trip, null=False, on_delete=models.PROTECT)
    check_code = models.ForeignKey(Check_code, null=False, on_delete=models.PROTECT)
    city = models.ForeignKey(City, null=False, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, null=False, on_delete=models.PROTECT)
    createdAt = models.DateTimeField(default=datetime.datetime.today, null=False)
    updatedAt = models.DateTimeField(default=datetime.datetime.today, null=False)
    price = models.IntegerField(null=False)


class Start_trip(models.Model):
    trip = models.ForeignKey(Trip, null=False, on_delete=models.PROTECT, related_name='start_trip')
    date = models.DateTimeField(default=datetime.datetime.today, null=False)
    pickup_address = models.CharField(max_length=100, null=False)
    city = models.ForeignKey(City, null=False, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, null=False, on_delete=models.PROTECT)
    pickup_location_type = models.CharField(max_length=10, default="Point", null=False)
    pickup_location_lat = models.DecimalField(max_digits=18, decimal_places=15, null=False)
    pickup_location_long = models.DecimalField(max_digits=18, decimal_places=15, null=False)


class Stop_trip(models.Model):
    trip = models.ForeignKey(Trip, null=False, on_delete=models.PROTECT, related_name='stop_trip')
    date = models.DateTimeField(null=True)
    pickup_address = models.CharField(max_length=100, null=False)
    city = models.ForeignKey(City, null=False, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, null=False, on_delete=models.PROTECT)
    pickup_location_type = models.CharField(max_length=10, default="Point", null=False)
    pickup_location_lat = models.DecimalField(max_digits=18, decimal_places=15, null=False)
    pickup_location_long = models.DecimalField(max_digits=18, decimal_places=15, null=False)


class Driver_location(models.Model):
    trip = models.ForeignKey(Trip, null=False, on_delete=models.PROTECT, related_name='driver_locationtrip')
    type = models.CharField(max_length=10, default="Point", null=False)
    lat = models.DecimalField(max_digits=18, decimal_places=15, null=False)
    long = models.DecimalField(max_digits=18, decimal_places=15, null=False)
