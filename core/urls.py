"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('booking.urls')),  # ✅ Yeh line ho
]
from django.contrib import admin
from django.urls import path
from booking.views import create_booking, get_bookings  # 👈 add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-booking/', create_booking, name='create_booking'),
    path('get-bookings/', get_bookings, name='get_bookings'),  # 👈 new
]