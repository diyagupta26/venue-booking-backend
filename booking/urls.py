from .views import RegisterView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
from django.urls import path
from .views import home, create_booking, get_bookings  # ✅ sab views import karo

urlpatterns = [
    path('', home),
    path('create-booking/', create_booking),
    path('get-bookings/', get_bookings),  # ✅ yeh naya API route
]
from django.urls import path
from .views import register_user, create_booking, get_bookings

urlpatterns = [
    path('register/', register_user),
    path('create-booking/', create_booking),
    path('get-bookings/', get_bookings),
]
from django.urls import path
from .views import home, create_booking, get_bookings

urlpatterns = [
    path('', home),  # 👈 yeh empty path ke liye hai
    path('create-booking/', create_booking),
    path('get-bookings/', get_bookings),
]

from django.urls import path
from .views import register_user, create_booking, get_bookings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', register_user),
    path('create-booking/', create_booking),
    path('get-bookings/', get_bookings),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
    path('register/', RegisterView.as_view()),  # 👈 user register
    path('create-booking/', create_booking),
    path('get-bookings/', get_bookings),

    # JWT Auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

from django.urls import path
from .views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view()),  # ✅ user register endpoint
    # tumhare existing URLs yahan honge jaise: create-booking, get-bookings
]

from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # other routes like create-booking, get-bookings...
]



from django.urls import path
from .views import RegisterView, LoginView, VenueListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('venues/', VenueListView.as_view(), name='venue-list'),
]


from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, VenueListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # ✅ JWT login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # ✅ Refresh token
    path('venues/', VenueListView.as_view(), name='venue-list'),
]

from django.urls import path
from .views import BookingCreateListView

urlpatterns = [
    path('bookings/', BookingCreateListView.as_view(), name='booking-list-create'),
]

from django.urls import path
from .views import RegisterView, LoginView, VenueCreateListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('api/bookings/', VenueCreateListView.as_view(), name='booking-list-create'),
]

from .views import VenueCreateListView

urlpatterns = [
    path('venues/', VenueCreateListView.as_view(), name='venue-list-create'),  # ✅ more accurate
]