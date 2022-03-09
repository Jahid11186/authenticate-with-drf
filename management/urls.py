from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import root

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root),
    path('registration/', include('registration.urls')),
    path('student/', include('student.urls')),
    path('profile/', include('self_profile.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
