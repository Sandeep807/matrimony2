from django.db.models import fields
from .models import *
from rest_framework import serializers

class RegistrationSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Registration
        fields=['id','profile_created_by','password','first_name',
        'last_name','email','mobile_number','is_verified','gender']

class BasicDetailsSerialiser(serializers.ModelSerializer):
    class Meta:
        model=BasicDetails
        fields='__all__'

class CasteDetailsSerialiser(serializers.ModelSerializer):
    class Meta:
        model=CasteDetails
        fields='__all__'

class PersonalDetailsSerialiser(serializers.ModelSerializer):
    class Meta:
        model=PersonalDetails
        fields='__all__'

class ProfessionalDetailsSerialiser(serializers.ModelSerializer):
    class Meta:
        model=ProfessionalDetails
        fields='__all__'

class PackageSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Package
        fields='__all__'

class PaymentSerialiser(serializers.ModelSerializer):
    class Meta:
        model=PaymentDetails
        fields='__all__'

class ImageSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields='__all__'

class LoginSerialiser(serializers.Serializer):
    mobile_number=serializers.CharField()
    password=serializers.CharField()

class PasswordSerialiser(serializers.Serializer):
    new_password=serializers.CharField()
    confirm_password=serializers.CharField()



