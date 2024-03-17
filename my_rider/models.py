# Create your models here.
from django.db import models


#Assignment -1
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"Profile of {self.user.username}"

#Assignment -3
class Ride(models.Model):
    pass  # Your Ride model definition

class Rating(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Rating for {self.ride}"

class Comment(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"Comment for {self.ride}"

#Assignment -2
class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.country}"


class Location(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.name}, {self.city}"



class Rider(models.Model):
    name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=50, choices=[('auto', 'Auto'), ('bike', 'Bike'), ('car', 'Car')])
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.vehicle_type})"

