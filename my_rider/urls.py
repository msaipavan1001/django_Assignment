from django.urls import path
from .views import RatingCreate, CommentCreate,CityListCreate, LocationListCreate

urlpatterns = [
    path('ratings/', RatingCreate.as_view(), name='rating-create'),
    path('comments/', CommentCreate.as_view(), name='comment-create'),
    path('cities/', CityListCreate.as_view(), name='city-list-create'),
    path('locations/', LocationListCreate.as_view(), name='location-list-create'),
    path('riders/', RiderListCreate.as_view(), name='rider-list-create'),
]
