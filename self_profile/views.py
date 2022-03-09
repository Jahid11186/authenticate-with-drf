from django.shortcuts import render
from student.models import Student
from teacher.models import Teacher
from .serializers import ProfileSerializer
from rest_framework import generics
from rest_framework.response import Response


# Create your views here.
def view_profile(request):
    return render(request, 'user_profile.html')


class ProfileViewSTD(generics.ListAPIView):
    permission_classes = []

    def get(self, request, id):
        data_val = Student.objects.filter(id=id).first()
        data_val = ProfileSerializer(data_val, many=False).data
        return Response(data_val)


# class ProfileViewTCHR(generics.ListAPIView):
#     permission_classes = []
#     def get(self, request, id):
#         data_val = Teacher.objects.filter(id=id).first()
#         data_val = ProfileSerializer(data_val, many=False).data
#         return Response(data_val)