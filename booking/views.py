from django.http import HttpResponse
from rest_framework.permissions import AllowAny

def home(request):
    return HttpResponse("Welcome to Venue Booking Backend")
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Booking

@csrf_exempt
def create_booking(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Dummy data handle kar rahe
        name = data.get('name')
        date = data.get('date')

        booking = Booking.objects.create(name=name, date=date)
        return JsonResponse({'message': 'Booking created successfully'})

    return JsonResponse({'error': 'Invalid request method'}, status=400)
from .models import Booking
from django.http import JsonResponse

def get_bookings(request):
    if request.method == 'GET':
        bookings = Booking.objects.all()
        data = [{'name': b.name, 'date': str(b.date)} for b in bookings]
        return JsonResponse(data, safe=False)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username is None or password is None:
        return Response({'error': 'Username and password required'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'User already exists'}, status=400)

    user = User.objects.create_user(username=username, password=password)
    return Response({'message': 'User registered successfully'}, status=201)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializer

@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User registered successfully'})
    return Response(serializer.errors, status=400)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Venue Booking Backend")

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]  # import from rest_framework.permissions
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Venue Booking Backend")


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Venue
from .serializers import VenueSerializer

class VenueListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        venues = Venue.objects.all()
        serializer = VenueSerializer(venues, many=True)
        return Response(serializer.data)
    
    from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
    

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser
from .models import Venue
from .serializers import VenueSerializer

class VenueCreateListView(ListCreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]  # ← instantiate kiya
        return []  # ← GET requests ke liye permission free
    

from rest_framework import generics
from .models import Booking
from .serializers import BookingSerializer

class BookingCreateListView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer