from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Rating, Comment,City, Location,Rider
from .serializers import RatingSerializer, CommentSerializer, CitySerializer, LocationSerializer,RiderSerializer,UserRegistrationSerializer

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

class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)