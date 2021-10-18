from django.shortcuts import render

# Create your views here.
from .serialiser import *
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from django.contrib.auth import authenticate
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework_simplejwt.tokens import RefreshToken 

from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class Register(viewsets.ModelViewSet):
    # authentication_classes=[JWTAuthentication]
    # permission_classes=[IsAuthenticated]
    queryset=Registration.objects.all()
    serializer_class=RegistrationSerialiser

    
class BasicDetail(viewsets.ModelViewSet):
    queryset=BasicDetails.objects.all()
    serializer_class=BasicDetailsSerialiser

class CasteDetail(viewsets.ModelViewSet):
    queryset=CasteDetails.objects.all()
    serializer_class=CasteDetailsSerialiser

class PersonalDetail(viewsets.ModelViewSet):
    queryset=PersonalDetails.objects.all()
    serializer_class=PersonalDetailsSerialiser

class ProfessionalDetail(viewsets.ModelViewSet):
    queryset=ProfessionalDetails.objects.all()
    serializer_class=ProfessionalDetailsSerialiser

class PackageDetail(viewsets.ModelViewSet):
    queryset=Package.objects.all()
    serializer_class=PackageSerialiser

class PaymentDetail(viewsets.ModelViewSet):
    queryset=PaymentDetails.objects.all()
    serializer_class=PaymentSerialiser

class ImageUpload(viewsets.ModelViewSet):
    queryset=Image.objects.all()
    serializer_class=ImageSerialiser


class Login(APIView):
    def post(self,request):
        try:
            data=request.data
            serialiser=LoginSerialiser(data=data)
            if serialiser.is_valid():
                mobile_number=serialiser.data['mobile_number']
                password=serialiser.data['password']
                register=Registration.objects.filter(mobile_number = mobile_number).first()
                if not register:
                    return Response(
                        {
                            'status':False,
                            'message':'user not found',
                            'data':{}
                        }
                    )
                user_obj = authenticate(mobile_number=mobile_number,password=password)
                if user_obj is None:
                    return Response({
                        'status':False,
                        'message':'Invalid username and password',
                        'data':{}
                    })
                token,_=Token.objects.get_or_create(user = user_obj)
                return Response({
                    'status':True,
                    'Message':'Login success',
                    'data':{
                         'token':str(token)
                    }
                })
        except Exception as e:
            # import sys, os
            # exc_type, exc_obj, exc_tb = sys.exc_info()
            # fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            # print(exc_type, fname, exc_tb.tb_lineno)
            print(e)
            return Response({
                'status':False,
                'message':'Something went wrong'
            })






class ChangePassword(APIView):
    def post(self,request):
        try:
            data=request.data
            #mobile_number=request.data.get['mobile_number']
            serialise=PasswordSerialiser(data=data)
            if serialise.is_valid():
                new_password=serialise.data['new_password']
                confirm_password=serialise.data['confirm_password']
                mobile_number=serialise.data['mobile_number']
                if confirm_password==new_password:
                        print(mobile_number)
                        obj=Registration.objects.filter(mobile_number=mobile_number).first()
                        if obj is not None:
                            old_password=serialise.data['old_password']
                            user=authenticate(mobile_number=mobile_number,password=old_password)
                            print(user)
                            if user:
                                print(user)
                                obj.set_password(new_password)
                                obj.save()
                                return Response({
                                    'status':'Success',
                                    'details':"password successfully"
                                })
                            return Response({
                                    'status':'False',
                                    'details':"old password missmatch"
                                })
                        return Response({
                                    'status':'False',
                                    'details':"username not found"
                                })
                return Response({
                                'status':'False',
                                'details':"new and confirm password missmatch"
                            })
            return Response({
                                'status':'False',
                                'details':serialise.errors
                            })
                        
        except Exception as e:
            print(e)
            return Response({'status':404,'message':'Something went wrong'})