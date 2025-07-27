from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()  # This will get CustomUser automatically

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')  # Add email if needed
        password = request.data.get('password')

        if username and password:
            try:
                User.objects.create_user(username=username, email=email, password=password)
                return Response({'message': 'User registered successfully'}, status=201)
            except Exception as e:
                return Response({'error': str(e)}, status=400)
        
        return Response({'error': 'Username and password are required'}, status=400)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            return Response({'message': 'Login successful'}, status=200)
        
        return Response({'error': 'Invalid credentials'}, status=401)
    
    from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from booking.models import CustomUser

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            # Generate JWT token
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Login successful',
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=200)

        return Response({'error': 'Invalid credentials'}, status=401)
