from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from taxi.models import *
# Register your models here.
admin.site.register(Registration)
admin.site.register(Package)
admin.site.register(Payment)
admin.site.register(DriverRegistration)
admin.site.register(Booking)
