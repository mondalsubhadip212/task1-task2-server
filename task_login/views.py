# custom import
from .models import User,UserDetails
from .signup import signup_verify

# django import
from django.contrib.auth import authenticate

# rest framework import
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# python import
import json

# Create your views here.

class Login(APIView):

    def post(self,request):
    
        try:
            User.objects.get(email=request.data['email'])
        except:
            return Response(
                status=status.HTTP_200_OK,
                data={
                    'error' : 'User Not Found'
                }
            )
        auth_user = authenticate(username=request.data['email'],password=request.data['password'])
        if auth_user:
            return Response(
                status=status.HTTP_200_OK,
                data={
                    'success' : 'Successfully Login'
                }
            )
        return Response(
            status=status.HTTP_200_OK,
            data={
                'error' : 'Wrong Password'
            }
        )


class Signup(APIView):

    def post(self,request):
        try:
            verify,current_user = signup_verify(request.data)
            current_user_details = UserDetails.objects.get(pk=current_user)
        except:
            return Response(
                status=status.HTTP_406_NOT_ACCEPTABLE,
                data={
                    'error' : 'email,username,phone_number,password can\'t be empty'
                }
            )
        if verify:
            details = {
                "username" : current_user.username,
                "email" : current_user.email,
                "phone number" : current_user_details.phone_number,
                "loacation" : current_user_details.address,
                "company name" : current_user_details.company_name,
                "client type" : current_user_details.client_type,
                "avg_revenue" : current_user_details.avg_revenue
            }
            return Response(
                status=status.HTTP_201_CREATED,
                data={
                    'success' : 'user created',
                    "details" : json.dumps(details)
                }
            )
        elif verify == 'password not match':
            return Response(
                status=status.HTTP_200_OK,
                data={
                    'error': 'password must match'
                }
            )
        return Response(
            status=status.HTTP_200_OK,
            data={
                "error" : "user already present"
            }
        )
