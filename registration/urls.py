from django.urls import path
from .views import sign_up, sign_in, sign_out, UserSignup, OTPCheck, UserSignIn

urlpatterns = [
    # API
    path('api/signup/', UserSignup.as_view()),
    path('api/otp_check/', OTPCheck.as_view()),
    path('api/signin/', UserSignIn.as_view()),

    # Function views
    path('signup/', sign_up),
    path('signin/', sign_in),
    path('signout/', sign_out)
]
