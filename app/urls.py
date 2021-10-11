from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'register',Register,basename='register')
router.register(r'basic_details',BasicDetail,basename='basic_details')
router.register(r'caste_details',CasteDetail,basename='caste_details')
router.register(r'personal_details',PersonalDetail,basename='personal_details')
router.register(r'professional_details',ProfessionalDetail,basename='professional_details')
router.register(r'package',PackageDetail,basename='package')
router.register(r'payment',PaymentDetail,basename='payment')
router.register(r'upload_image',ImageUpload,basename='upload_image')

urlpatterns = [
    path('loginapp/',Login.as_view()),
    path('changeapp/',ChangePassword.as_view()),
]
urlpatterns += router.urls