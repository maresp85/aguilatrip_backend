from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (City, Country, Trip, Start_trip, Stop_trip, Driver_location,
                     Status_trip)

from datetime import date

import locale

locale.setlocale(locale.LC_TIME, 'es')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('name',)


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('name',)


class Start_tripSerializer(serializers.ModelSerializer):
    city = CitySerializer(many=False)

    class Meta:
        model = Start_trip
        fields = ('date', 'pickup_address', 'city', 'pickup_location_type',
                  'pickup_location_lat', 'pickup_location_long')


class Stop_tripSerializer(serializers.ModelSerializer):
    city = CitySerializer(many=False)

    class Meta:
        model = Stop_trip
        fields = ('date', 'pickup_address', 'city', 'pickup_location_type',
                  'pickup_location_lat', 'pickup_location_long')


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status_trip
        fields = ('name',)


class Driver_locationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver_location
        fields = ('type', 'lat', 'long')


class TripSerializer(serializers.ModelSerializer):
    start = Start_tripSerializer(source='start_trip', many=True)
    end = Stop_tripSerializer(source='stop_trip', many=True)
    driver_location = Driver_locationSerializer(source='driver_locationtrip', many=True)
    city = CitySerializer(many=False)
    country = CountrySerializer(many=False)
    status = StatusSerializer(many=False)
    passenger = UserSerializer(many=False,)
    driver = UserSerializer(many=False,)

    class Meta:
        model = Trip
        fields = ('start', 'end', 'city', 'country', 'passenger', 'driver',
                  'car', 'status', 'check_code', 'createdAt', 'updatedAt',
                  'price', 'driver_location', 'id')


class TripSerializerPut(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = ('driver', 'car', 'updatedAt', 'status')
