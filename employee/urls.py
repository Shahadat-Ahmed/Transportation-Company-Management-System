from django.urls import path
from .views import driver_home

urlpatterns = [
    path('driver_homepage/', driver_homep, name='driver_home'),
]