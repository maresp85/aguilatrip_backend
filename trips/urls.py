from django.urls import path, include
from . import views

urlpatterns = [
     path('', views.TripView.as_view(), name=''),
     path('<int:pk>/', views.TripView.as_view(), name=''),
     path('count/', views.TripCount.as_view(), name='count'),
     path('countcity/<int:city>/', views.TripCountCity.as_view(), name='countcity'),
     path('driver_location/', views.Driver_locationView.as_view(), name='driver_location'),
     path('end/<int:pk>/', views.EndTrip.as_view(), name='end'),
     path('loaddata/', views.LoadData.as_view(), name='loaddata'),     
]
