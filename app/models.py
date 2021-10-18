from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from .managers import *
from .Options import *
# Create your models here.


class Registration(AbstractUser):

    """To store user details"""
    gender_choices=(('Select Options','Select Options'),('Male','Male'),('Female','Female'))
    username=None
    mobile_number=models.CharField(max_length=15,unique=True)
    is_verified=models.BooleanField(default=False)
    profile_created_by=models.CharField(max_length=100,choices=profile_choices)
    gender=models.CharField(max_length=15,choices=gender_choices)
    
    USERNAME_FIELD='mobile_number'
    REQUIRED_FIELDS=[]
    objects=UserManager()

class BasicDetails(models.Model):
    dob=models.DateField(null=True,blank=True)
    religion=models.CharField(max_length=200,choices=religion_choices)
    mother_tongue=models.CharField(max_length=100,choices=tongue)
    email=models.CharField(max_length=100)
    register=models.ForeignKey(Registration,on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Package(models.Model):

    """To store package details"""

    mem_choices=(('Select Options','Select Options'),('Silver','Silver'),('Gold','Gold'),('Diamond','Diamond'))
    amount=models.IntegerField()
    membership=models.CharField(max_length=100,choices=mem_choices)

class PaymentDetails(models.Model):

    """To store payment details"""
    transaction_id=models.CharField(max_length=100,null=True,blank=True)
    order_id=models.CharField(max_length=100,null=True,blank=True)
    payment_signature=models.CharField(max_length=100,null=True,blank=True)
    is_paid=models.BooleanField(default=False)
    register=models.ForeignKey(Registration,on_delete=models.CASCADE)
    package=models.ForeignKey(Package,null=True,blank=True,on_delete=models.CASCADE)

class CasteDetails(models.Model):
    caste=models.CharField(max_length=1000,choices=caste_choices)
    dosh=models.CharField(max_length=100,choices=dosh_choices)
    register=models.ForeignKey(Registration,on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class PersonalDetails(models.Model):
    height=models.CharField(max_length=100)
    marital_status=models.CharField(max_length=100,choices=status_choices)
    any_disability=models.CharField(max_length=100,choices=disability_choices)
    family_status=models.CharField(max_length=100,choices=family_choices)
    family_type=models.CharField(max_length=100,choices=family_type_choices)
    family_value=models.CharField(max_length=100,choices=family_value_choices)
    register=models.ForeignKey(Registration,on_delete=models.CASCADE)

class ProfessionalDetails(models.Model):
    education=models.CharField(max_length=1000,choices=education_choices)
    employed_in=models.CharField(max_length=100,choices=employee_choices)
    occupation=models.CharField(max_length=100,choices=occupation_choices)
    annual_income=models.CharField(max_length=1000,choices=annual_income_choices)
    work_location=models.CharField(max_length=100,choices=work_choices)
    residing_state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    register=models.ForeignKey(Registration,on_delete=models.CASCADE)

class Image(models.Model):
    pic=models.ImageField(upload_to='image',null=True,blank=True)
    register=models.OneToOneField(Registration,on_delete=models.CASCADE)