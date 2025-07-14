from django.urls import path
from . import views

urlpatterns = [
    path('create-booking/', views.create_booking, name='create_booking'),
    path('get-venues/', views.get_venues, name='get_venues'),  # ✅ Yeh line zaroor ho
]
from django.urls import path
from . import views

urlpatterns = [
    path('create-booking/', views.create_booking),
    path('get-venues/', views.get_venues),
    path('submit-feedback/', views.submit_feedback),  # ✅ Yeh line zaroor ho
]
from django.urls import path
from . import views

urlpatterns = [
    path('create-booking/', views.create_booking),
    path('get-venues/', views.get_venues),
    path('submit-feedback/', views.submit_feedback),
    path('get-bookings/', views.get_bookings),  # ✅ NEW
]
from django.urls import path
from .views import get_bookings

urlpatterns = [
    path('get-bookings/', get_bookings, name='get_bookings'),
]