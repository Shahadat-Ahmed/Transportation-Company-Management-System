from django.urls import path
from .views import admin_homepage

urlpatterns = [
    path('admin-homepage/', admin_homepage, name='admin_homepage'),
]