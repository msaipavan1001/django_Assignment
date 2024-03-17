from rest_framework import serializers
from .models import Rating, Comment,City, Location,Rider,UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'address']

class UserRegistrationSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', {})
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user, **profile_data)
        return user

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