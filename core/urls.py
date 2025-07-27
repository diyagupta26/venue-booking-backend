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
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Venue Booking Backend")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('create-booking/', create_booking),
    path('get-bookings/', get_bookings),
]
from booking.views import get_bookings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-bookings/', get_bookings, name='get_bookings'),
]
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Venue Booking Backend")

urlpatterns = [
    path('', home),  # 👈 this handles the root URL
    path('admin/', admin.site.urls),
    path('get-bookings/', get_bookings, name='get_bookings'),
]
from django.contrib import admin
from django.urls import path, include  # ✅ include import karna mat bhoolna

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('booking.urls')),  # ✅ booking app ke urls link kar rahe hain
]
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('booking.urls')),  # 👈 already hai
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # 👈 login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # 👈 token renew
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('booking.urls')),  # 👈 yeh line zaroori hai
]

from django.contrib import admin
from django.urls import path, include
from booking.views import home  # 👈 yeh function agar tumhare views.py mein hai

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # 👈 root path pe home view call hoga
    path('register/', include('booking.urls')),  # baki urls booking app mein
]


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('', include('booking.urls')),

    # 🔐 JWT Auth URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

from django.urls import path
from .views import RegisterView, LoginView  # LoginView ko bhi import karo

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),  # ✅ yeh line add karo
]

from django.urls import path
from core.views import RegisterView, LoginView  # ✅ ab yeh kaam karega

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]

from django.contrib import admin
from django.urls import path, include  # 👈 yeh line zaruri hai

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('booking.urls')),  # 👈 yeh line add karo agar nahi hai
]

from django.contrib import admin
from django.urls import path, include
from booking.views import home
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('', include('booking.urls')),  # ✅ yeh correctly add kiya gaya hai
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

path('api/', include('booking.urls'))