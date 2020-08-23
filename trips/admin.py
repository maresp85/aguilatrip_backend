from django.contrib import admin
from .models import (Country, City, Car, Driver_location, Status_trip,
                     Check_code, Trip, Start_trip, Stop_trip)

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Car)
admin.site.register(Driver_location)
admin.site.register(Status_trip)
admin.site.register(Check_code)
admin.site.register(Trip)
admin.site.register(Start_trip)
admin.site.register(Stop_trip)
