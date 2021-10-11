from django.db import models
from app.models import Registration
# Create your models here.
class DriverRegistration(Registration):

    """To store details of driver"""
    licence=models.CharField(max_length=20)
    aadhar_card=models.IntegerField()
    pan_card=models.CharField(max_length=20)
    profile_image=models.ImageField(upload_to="driver",null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)



class Booking(models.Model):

    """To store booking details"""

    vehicle=(('Select Options','Select Options'),('TOYOTA ETIOS','TOYOTA ETIOS'),('SWIFT DZIRE','SWIFT DZIRE')
    ,('MAHINDRA VERITO','MAHINDRA VERITO'),('INNOVA 6+1','INNOVA 6+1'),
    ('INNOVA 7+1','INNOVA 7+1'),('TEMPO TRAVELLER','TEMPO TRAVELLER'),
    ('MINI BUS','MINI BUS'),('SEDAN','SEDAN'),('HATCHBACK','HATCHBACK'))
    
    name=models.CharField(max_length=100)
    mobile_number=models.CharField(max_length=15)
    source_address=models.TextField()
    destination_address=models.TextField()
    booking_date=models.DateField(null=True,blank=True)
    booking_time=models.TimeField()
    type_vehicle=models.CharField(max_length=100,choices=vehicle)
    is_cancel=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

class Payment(models.Model):
    booking=models.ForeignKey(Booking,on_delete=models.CASCADE)
    registration=models.ForeignKey(Registration,on_delete=models.CASCADE)
    is_paid=models.BooleanField(default=False)
    oder_id=models.CharField(max_length=100)