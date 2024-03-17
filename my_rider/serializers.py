from rest_framework import serializers
from .models import Rating, Comment,City, Location,Rider

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'ride', 'rating', 'comment']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'ride', 'comment']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'country']

class LocationSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Location
        fields = ['id', 'city', 'name', 'latitude', 'longitude']

class RiderSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Rider
        fields = ['id', 'name', 'vehicle_type', 'city']