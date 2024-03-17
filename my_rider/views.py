from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from .models import Rating, Comment,City, Location,Rider
from .serializers import RatingSerializer, CommentSerializer, CitySerializer, LocationSerializer,RiderSerializer

class RatingCreate(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CityListCreate(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class LocationListCreate(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class RiderListCreate(generics.ListCreateAPIView):
    queryset = Rider.objects.all()
    serializer_class = RiderSerializer