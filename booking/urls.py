from django.contrib import admin
from django.urls import path, include
from core.views import home, RegisterView, LoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('booking/', include('booking.urls')),  # Forward to booking app
]
from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('venues/', views.venue_list, name='venue-list'),
    path('book/<int:venue_id>/', views.book_venue, name='book-venue'),
]
