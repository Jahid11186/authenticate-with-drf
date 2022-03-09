from django.urls import path
from .views import view_profile, ProfileViewSTD

urlpatterns = [
    # API
    path('student/<str:id>/', ProfileViewSTD.as_view()),
    # path('teacher/<str:id>/', ProfileViewTCHR.as_view()),

    # function views
    path('view/', view_profile),
]