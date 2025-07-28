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