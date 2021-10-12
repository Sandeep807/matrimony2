from django.shortcuts import render
from .serialiser import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class DriverRegister(viewsets.ModelViewSet):
    queryset=DriverRegistration.objects.all()
    serializer_class=DriverRegistrationSerialiser

# class BookVehicle(viewsets.ModelViewSet):
#     queryset=Booking.objects.all()
#     serializer_class=BookingSerialiser

class PaymentDetail(viewsets.ModelViewSet):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerialiser

class BookingVehicle(APIView):
    
    def post(self,request):
        try:
            data=request.data
            serialiser=BookingSerialiser(data=data)
            if serialiser.is_valid():
                return Response(serialiser.data,status=status.HTTP_200_OK)
            else:
                return Response({'error':serialiser.errors,'Message':'Invalid data'})
        except Exception as e:
            print(e)
            return Response({'error':serialiser.errors,'Message':'Something went wrong'})
    
    def patch(self,request):
        try:
            data=request.data
            check=Booking.objects.get(id=data.get('id'))
            check.is_cancel=True
            check.save()
            return Response({'Message':'Booking cancel'})  
        except Exception as e:
            print(e)
            return Response({'Message':'Something went wrong'})

class Login(APIView):
    def post(self,request):
        try:
            data=request.data
            serialiser=DriverLoginSerialiser(data=data)
            if serialiser.is_valid():
                mobile_number=serialiser.data['mobile_number']
                password=serialiser.data['password']
                if not DriverRegistration.objects.filter(mobile_number = mobile_number).exists():
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
                        'message':'Invalid password',
                        'data':{}
                    })
                token=Token.objects.get_or_create(user = user_obj)
                return Response({
                    'status':True,
                    'Message':'Login success',
                    'data':{
                        # 'token':str(token)
                    }
                })
        except Exception as e:
            print(e)
            return Response({
                'status':False,
                'message':'Something went wrong'
            })

class ChangePassword(APIView):
    def post(self,request):
        try:
            data=request.data
            serialise=PasswordSerialiser(data=data)
            if(serialise.is_valid()):
                new_password=serialise.data['new_password']
                confirm_password=serialise.data['confirm_password']
                if(new_password==confirm_password):
                    serialise.save()
                    return Response({'status':200,'message':'Password has been change successful','Detail':serialise.data})
                else:
                    return Response({'status':400,'error':serialise.errors,'message':'Not match password and confirm password'})
            else:
                return Response({'status':400,'message':"Invalid data"})
        except Exception as e:
            print(e)
            return Response({'status':404,'message':'Something went wrong'})