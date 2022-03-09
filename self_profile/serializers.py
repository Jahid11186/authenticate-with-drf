from rest_framework import serializers
from student.models import Student
from teacher.models import Teacher


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['role', 'id', 'full_name', 'birth_date',
                  'email', 'phone',
                  'father_name', 'mother_name',
                  'gender', 'religion', 'address',
                  'blood_group', 'nationality', 'profile_pic'
                  ]
