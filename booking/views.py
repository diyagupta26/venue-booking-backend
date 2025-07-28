from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Venue, Booking
from .serializers import VenueSerializer, BookingSerializer

# ✅ List all venues OR create new one
class VenueCreateListView(generics.ListCreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]  # Only admin can POST
        return [AllowAny()]       # Anyone can GET

# ✅ Booking create/list view
class BookingCreateListView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]
    from django.http import JsonResponse
from .models import Venue

def venue_list(request):
    venues = Venue.objects.all()
    data = []
    for v in venues:
        data.append({
            'id': v.id,
            'name': v.name,
            'location': v.location,
            'capacity': v.capacity,
        })
    return JsonResponse(data, safe=False)
from django.http import JsonResponse

def book_venue(request, venue_id):
    return JsonResponse({'message': f'Booking venue with ID {venue_id}'})