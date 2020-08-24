from django.shortcuts import render
from django.contrib.auth.models import User
from .models import (Trip, Car, Status_trip, City, Country,
                     Start_trip, Stop_trip, Driver_location)
from .serializers import (TripSerializer, TripSerializerPut, Driver_locationSerializer)
#API rest_framework
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

import datetime
import json

class TripCount(APIView):

    """ Count Trips """
    def get(self, request, format=None):

        trip = Trip.objects.count()
        return Response(trip, status=status.HTTP_200_OK)


class TripCountCity(APIView):

    """  Count Trips by City """
    def get(self, request, city, format=None):

        trip = Trip.objects.filter(city_id=city).count()
        return Response(trip, status=status.HTTP_200_OK)


class Driver_locationView(APIView):

    """ Create or update driver location """
    def post(self, request, format=None):

        lat = request.data['lat']
        long = request.data['long']
        type = request.data['type']
        trip = Trip.objects.get(pk=request.data['trip'])
        try:
            driver_location = Driver_location.objects.get(trip=trip)
            driver_location.lat = lat
            driver_location.long = long
            driver_location.type = type
            driver_location.save()
        except:
            driver_location = Driver_location.objects.create(trip=trip,
                                                             type=type,
                                                             lat=lat,
                                                             long=long)
        serializer = Driver_locationSerializer(driver_location, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EndTrip(APIView):

    ''' End a trip '''
    def put(self, request, pk, format=None):

        try:
            trip = Trip.objects.get(pk=pk)
            status_trip = Status_trip.objects.get(pk=4) #End
            trip.updatedAt = datetime.datetime.now()
            trip.status = status_trip
            trip.save()
            stop_trip = Stop_trip.objects.get(trip=trip)
            stop_trip.date = datetime.datetime.now()
            stop_trip.save()
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        serializer = TripSerializer(trip, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TripView(APIView):

    """ Return all Trips """
    def get(self, request, format=None):

        trip = Trip.objects.all()

        #pagination
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(trip, request)

        serializer = TripSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    """ Create a new Trip """
    def post(self, request, format=None):

        try:
            passenger = User.objects.get(id=request.data['passenger'])
            status_trip = Status_trip.objects.get(id=request.data['status'])
            city = City.objects.get(id=request.data['city'])
            country = Country.objects.get(id=request.data['country'])
            #create trip
            trip = Trip.objects.create(passenger=passenger,
                                       status=status_trip,
                                       check_code=request.data['check_code'],
                                       city=city,
                                       country=country,
                                       price=request.data['price'])
            #create start
            Start_trip.objects.create(trip=trip,
                                      pickup_address=request.data['address'],
                                      city=city,
                                      country=country,
                                      pickup_location_lat=request.data['start_lat'],
                                      pickup_location_long=request.data['stop_long'])
            #create end
            Stop_trip.objects.create(trip=trip,
                                     pickup_address=request.data['address_end'],
                                     city=city,
                                     country=country,
                                     pickup_location_lat=request.data['stop_lat'],
                                     pickup_location_long=request.data['stop_long'])
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        serializer = TripSerializer(trip, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    ''' Edit a Trip '''
    def put(self, request, pk, format=None):

        trip = Trip.objects.get(pk=pk)
        request.data['updatedAt'] = datetime.datetime.now()
        serializer = TripSerializerPut(trip, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoadData(APIView):

    def get(self, request, format=None):
        data = json.load(open('trips.json', 'r', encoding='utf-8'))
        passenger = User.objects.get(id=6)
        driver = User.objects.get(id=8)
        country = Country.objects.get(id=1)
        for x in data['trips']:
            try:
                city = City.objects.get(name=x['city']['name'])
                status_trip = Status_trip.objects.get(name=x['status'])
                try:
                    car = Car.objects.get(plate=x['car']['plate'])
                except:
                    car = Car.objects.create(plate=x['car']['plate'])
                #create trip
                trip = Trip.objects.create(passenger=passenger,
                                           driver=driver,
                                           status=status_trip,
                                           check_code=x['check_code'],
                                           city=city,
                                           car=car,
                                           country=country,
                                           price=x['price'],
                                           createdAt=x['createdAt']['$date'],
                                           updatedAt=x['updatedAt']['$date'])
                #create start
                Start_trip.objects.create(trip=trip,
                                          pickup_address=x['start']['pickup_address'],
                                          date=x['start']['date']['$date'],
                                          city=city,
                                          country=country,
                                          pickup_location_lat=x['start']['pickup_location']['coordinates'][0],
                                          pickup_location_long=x['start']['pickup_location']['coordinates'][1])
                #create end
                try:
                    enddate = x['end']['date']['$date']
                except:
                    enddate = None
                Stop_trip.objects.create(trip=trip,
                                         pickup_address=x['end']['pickup_address'],
                                         date=enddate,
                                         city=city,
                                         country=country,
                                         pickup_location_lat=x['end']['pickup_location']['coordinates'][0],
                                         pickup_location_long=x['end']['pickup_location']['coordinates'][1])
                Driver_location.objects.create(trip=trip,
                                               type=x['driver_location']['type'],
                                               lat=x['driver_location']['coordinates'][0],
                                               long=x['driver_location']['coordinates'][1])
            except:
                print("error")
        return Response('OK')
