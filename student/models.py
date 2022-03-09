from django.db import models
from .strings import *
from django.contrib.auth.models import User
from registration.models import ManagementModel


# Create your models here.
class Student(ManagementModel):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.PROTECT)
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True, max_length=100)
    phone = models.CharField(null=True, blank=True, max_length=100)
    father_name = models.CharField(max_length=100, null=True, blank=True)
    mother_name=models.CharField(max_length=100, null=True, blank=True)
    gender=models.CharField(max_length=20, choices=GENDER_CHOICE, null=True, blank=True)
    religion=models.CharField(max_length=20, choices=RELIGION_CHOICE, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    blood_group= models.CharField(max_length=10, choices=BG_CHOICE, null=True,blank=True)
    nationality = models.CharField(default='Bangladeshi', choices=NATIONALITY_CHOICE, max_length=50)
    profile_pic = models.ImageField(upload_to='student/profile_pic',null=True,blank=True)
    otp = models.CharField(max_length=10,null=True,blank=True)

    def __str__(self):
        return self.full_name + str(self.id)
