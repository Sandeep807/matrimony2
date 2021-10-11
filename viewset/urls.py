from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('matri/',include('app.urls')),
    path('taxi/',include('taxi.urls')),
]



