from django.urls import path
from .views import my_profile

urlpatterns = [
    path('myself/', my_profile),
]