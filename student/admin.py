from django.contrib import admin
from .models import Student


# ModelAdmin
class StudentAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = Student.objects.filter().order_by('id')
        return queryset

    fields = [
        ("role"),
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
admin.site.register(Student, StudentAdmin)