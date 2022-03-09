from django.shortcuts import render
from .models import Student
from rest_framework import generics
from rest_framework.response import Response


# Create your views here.
def my_profile(request):
    return render(request, 'profile _form.html')
