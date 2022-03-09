from django.contrib import admin
from .models import Teacher


# ModelAdmin
class TeacherAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = Teacher.objects.filter().order_by('id')
        return queryset

    fields = [
        "role",
        ("full_name", 'user'),
        ("email", "phone"),
        ("father_name", "mother_name"),
        ("birth_date", "blood_group", "gender"),
        ("nationality", "religion"),
        "address",
        "profile_pic",
        "otp"
    ]

    list_display = ["id", "full_name"]
    list_per_page = 10


# Register Model
admin.site.register(Teacher, TeacherAdmin)