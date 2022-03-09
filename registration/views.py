from django.shortcuts import render
from student.models import Student
from teacher.models import Teacher
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password, check_password
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.http import HttpResponseRedirect


# Create your views here.
def sign_up(request):
    return render(request, 'signup.html')


def sign_in(request):
    return render(request, 'signin.html')


def sign_out(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('access')
    response.delete_cookie('user_name')
    response.delete_cookie('main_name')
    return response


# OTP sending mail
def send_otp(to, subject, body):
    smtp_server = 'smtp.gmail.com'
    smtp_port = '465'
    sender_email = 'csq.jahid@gmail.com'
    sender_password = 'jahidinf_86'
    server = None
    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.ehlo()
        server.login(sender_email, sender_password)
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['to'] = to
        msg['Subject'] = subject

        html = """\
                <html>
                    <head></head>
                    <body>
                """
        html += body.replace('\r\n', '<br />\r\n')
        """
            </body>
        </html>
        """
        msg.attach(MIMEText(html, 'html'))
        server.sendmail(
            from_addr=sender_email,
            to_addrs=to,
            msg=msg.as_string()
        )
        print("OTP sent")
    except Exception as e:
        print(str(e))
    finally:
        if server is not None:
            server.quit()


# sign up & OTP check API
'''
class UserSignup(generics.ListAPIView):
    permission_classes = []

    def post(self, request):
        result = {}
        try:
            data = json.loads(request.body)
            if 'full_name' not in data or data['full_name'] == '':
                result['message'] = 'Full name can not be null'
                result['error'] = 'Full name'
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
            if 'email' not in data or data['email'] == '':
                result['message'] = 'Email can not be null'
                result['error'] = 'Email'
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
            if 'phone' not in data or data['phone'] == '':
                result['message'] = 'Phone number can not be null'
                result['error'] = 'Phone'
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
            if 'password' not in data or data['password'] == '':
                result['message'] = 'Password can not be null'
                result['error'] = 'Password'
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.filter(username=data['email']).first()
            if not user:
                user = User()
                user.username = data['email']
                user.email = data['email']
                user.first_name = data['full_name']
                user.password = make_password(data['password'])
                user.is_active = False
                user.save()
                otp_generate = random.randint(500000, 900000)
                student = Student()
                student.user = user
                student.full_name = data['full_name']
                student.email = data['email']
                student.otp = otp_generate
                student.save()
                send_otp(data['email'], 'Sign Up otp:', 'OTP:' + str(otp_generate))
                result = {
                    'status': status.HTTP_200_OK,
                    'Message': 'Success',
                    'email': data['email']
                }
                return Response(result)
        except Exception as e:
            return Response("Exception Occurred")
        return Response("True")
'''


class UserSignup(generics.ListAPIView):
    permission_classes = []

    def post(self, request):
        result = {}
        try:
            # data = json.loads(request.body)
            data = request.data

            if 'role' not in data or data['role'] == '':
                result['message'] = 'Role should be selected'
                result['error'] = 'Role'
            if 'full_name' not in data or data['full_name'] == '':
                result['message'] = 'Full name can not be null'
                result['error'] = 'Full name'
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
            if 'email' not in data or data['email'] == '':
                result['message'] = 'Email can not be null'
                result['error'] = 'Email'
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
            if 'phone' not in data or data['phone'] == '':
                result['message'] = 'Phone number can not be null'
                result['error'] = 'Phone'
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
            if 'password' not in data or data['password'] == '':
                result['message'] = 'Password can not be null'
                result['error'] = 'Password'
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.filter(username=data['email']).first()
            print("user:------------")
            print(user)
            if not user:
                user = User()
                user.username = data['email']
                user.email = data['email']
                user.first_name = data['full_name']
                user.password = make_password(data['password'])
                user.is_active = False
                user.save()
                otp_generate = random.randint(500000, 900000)
                if data['role'] == 'Student':
                    student = Student()
                    student.role = data['role']
                    student.user = user
                    student.full_name = data['full_name']
                    student.email = data['email']
                    student.otp = otp_generate
                    student.save()
                    send_otp(data['email'], 'Sign Up otp:', 'OTP:' + str(otp_generate))
                    result = {
                        'status': status.HTTP_200_OK,
                        'Message': 'Success',
                        'email': data['email'],
                        'role': data['role'],
                    }
                    return Response(result)

                if data['role'] == 'Teacher':
                    teacher = Teacher()
                    teacher.role = data['role']
                    teacher.user = user
                    teacher.full_name = data['full_name']
                    teacher.email = data['email']
                    teacher.otp = otp_generate
                    teacher.save()
                    send_otp(data['email'], 'Sign Up otp:', 'OTP:' + str(otp_generate))
                    result = {
                        'status': status.HTTP_200_OK,
                        'Message': 'Success',
                        'email': data['email'],
                        'role': data['role'],
                    }
                    return Response(result)

        except Exception as e:
            result = {}
            result['status'] = status.HTTP_400_BAD_REQUEST
            result['message'] = str(e)
            return Response(result)




'''
class OTPCheck(generics.ListAPIView):
    permission_classes = []

    def put(self, request):
        result = {}
        try:
            data = json.loads(request.body)
            if 'email' not in data or data['email'] == '':
                result['message'] = 'Email can not be null'
                result['error'] == ['Email']
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            if 'otp' not in data or data['otp'] == '':
                result['message'] = 'OTP can not be null'
                result['error'] = 'OTP'
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.filter(username=data['email']).first()
            if not user:
                result['message'] = 'Please create a account'
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
            elif user.is_active:
                result['message'] = 'You already created account'
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
            else:
                student = Student.objects.filter(user=user).first()
                if student.otp == data['otp']:
                    user.is_active = True
                    user.save()
                    student.otp = ''
                    student.save()
                    result = {
                        'message': 'SUCCESS',
                        'status': status.HTTP_200_OK
                    }
                    return Response(result)
                else:
                    result = {
                        'status': status.HTTP_400_BAD_REQUEST,
                        'message': 'OTP did not match',
                        'error': 'OTP'
                    }
                    return Response(result)
        except Exception as e:
            result = {'message': str(e)}
            return Response(result)
'''


class OTPCheck(generics.ListAPIView):
    permission_classes = []

    def put(self, request):
        result = {}
        try:
            #data = json.loads(request.body)
            data = json.loads(request.body)

            if 'role' not in data or data['role'] == '':
                result['message'] = 'Role can not be null'
                result['error'] = 'Role'
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            if 'email' not in data or data['email'] == '':
                result['message'] = 'Email can not be null'
                result['error'] = 'Email'
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            if 'otp' not in data or data['otp'] == '':
                result['message'] = 'OTP can not be null'
                result['error'] = 'OTP'
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.filter(username=data['email']).first()
            if not user:
                result['message'] = 'Please create a account'
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
            elif user.is_active:
                result['message'] = 'You already created account'
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
            else:
                if data['role'] == 'Student':
                    student = Student.objects.filter(user=user).first()
                    if student.otp == data['otp']:
                        user.is_active = True
                        user.save()
                        student.otp = ''
                        student.save()
                        result = {
                            'message': 'SUCCESS',
                            'status': status.HTTP_200_OK
                        }
                        return Response(result)
                    else:
                        result = {
                            'status': status.HTTP_400_BAD_REQUEST,
                            'message': 'OTP did not match',
                            'error': 'OTP'
                        }
                        return Response(result)

                elif data['role'] == 'Teacher':
                    teacher = Teacher.objects.filter(user=user).first()
                    if teacher.otp == data['otp']:
                        user.is_active = True
                        user.save()
                        teacher.otp = ''
                        teacher.save()
                        result = {
                            'message': 'SUCCESS',
                            'status': status.HTTP_200_OK
                        }
                        return Response(result)
                    else:
                        result = {
                            'status': status.HTTP_400_BAD_REQUEST,
                            'message': 'OTP did not match',
                            'error': 'OTP'
                        }
                        return Response(result)
        except Exception as e:
            result = {'message': str(e)}
            return Response(result)


# Sign in API
'''
class UserSignIn(generics.ListAPIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        result = {}
        try:
            data = json.loads(request.body)
            print(data)
            if 'role' not in data or data['role']=='':
                result['message']="choose your role"
                result['Error']="Role"
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            if 'email' not in data or data['email']=='':
                result['message']="Email can not be null."
                result['Error']="Email"
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            if 'password' not in data or data['password'] == '':
                result['message'] = "Password can not be null."
                result['Error'] = "Password"
                return Response(result,status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.filter(username=data['email']).first()
            print("USER----------")
            print(user)
            if not user:
                result = {
                    'message': 'Please create a account'
                }
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
            elif not user.is_active:
                result = {
                    'message': 'Please activate your account'
                }
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
            else:
                if data['role'] == 'Student':
                    if not check_password(data['password'], user.password):
                        result = {
                            'message': "Invalid Credentials"
                        }
                        return Response(result, status=status.HTTP_401_UNAUTHORIZED)
                    else:
                        student = Student.objects.filter(user=user).first()
                        token = RefreshToken.for_user(user)
                        data = {
                            'user_name': user.username,
                            'main_name': user.first_name,
                            'access': str(token.access_token),
                            'token': str(token),
                            'status': status.HTTP_200_OK
                        }
                        return Response(data)

                elif data['role'] == 'Teacher':
                    if not check_password(data['password'], user.password):
                        result = {
                            'message': "Invalid Credentials"
                        }
                        return Response(result, status=status.HTTP_401_UNAUTHORIZED)
                    else:
                        teacher = Teacher.objects.filter(user=user).first()
                        token = RefreshToken.for_user(user)
                        data = {
                            'user_name': user.username,
                            'main_name': user.first_name,
                            'access': str(token.access_token),
                            'token': str(token),
                            'status': status.HTTP_200_OK
                        }
                        return Response(data)
        except Exception as e:
            result = {}
            result['status'] = status.HTTP_400_BAD_REQUEST
            result['message'] = str(e)
            return Response(result)
'''


class UserSignIn(generics.ListAPIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        result = {}
        try:
            data = json.loads(request.body)
            print(data)
            if 'role' not in data or data['role']=='':
                result['message']="choose your role"
                result['Error']="Role"
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            if 'email' not in data or data['email']=='':
                result['message']="Email can not be null."
                result['Error']="Email"
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

            if 'password' not in data or data['password'] == '':
                result['message'] = "Password can not be null."
                result['Error'] = "Password"
                return Response(result,status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.filter(username=data['email']).first()
            print("USER----------")
            print(user)
            if not user:
                result = {
                    'message': 'Please create a account'
                }
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
            elif not user.is_active:
                result = {
                    'message': 'Please activate your account'
                }
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
            else:
                if data['role'] == 'Student':
                    if not check_password(data['password'], user.password):
                        result = {
                            'message': "Invalid Credentials"
                        }
                        return Response(result, status=status.HTTP_401_UNAUTHORIZED)
                    else:
                        student = Student.objects.filter(user=user).first()
                        token = RefreshToken.for_user(user)
                        data = {
                            'user_name': user.username,
                            'user_id': str(student.id),
                            'user_role': student.role,
                            'main_name': user.first_name,
                            'access': str(token.access_token),
                            'token': str(token),
                            'status': status.HTTP_200_OK
                        }
                        return Response(data)

                elif data['role'] == 'Teacher':
                    if not check_password(data['password'], user.password):
                        result = {
                            'message': "Invalid Credentials"
                        }
                        return Response(result, status=status.HTTP_401_UNAUTHORIZED)
                    else:
                        teacher = Teacher.objects.filter(user=user).first()
                        token = RefreshToken.for_user(user)
                        data = {
                            'user_name': user.username,
                            'user_id': str(teacher.id),
                            'user_role': teacher.role,
                            'main_name': user.first_name,
                            'access': str(token.access_token),
                            'token': str(token),
                            'status': status.HTTP_200_OK
                        }
                        return Response(data)
        except Exception as e:
            result = {}
            result['status'] = status.HTTP_400_BAD_REQUEST
            result['message'] = str(e)
            return Response(result)
