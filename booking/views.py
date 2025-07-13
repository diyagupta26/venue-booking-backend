from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Booking, Venue

@csrf_exempt
def create_booking(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        try:
            venue = Venue.objects.get(id=data['venue_id'])
            booking = Booking.objects.create(
                venue=venue,
                booked_by=data['booked_by'],
                date=data['date']
            )
            return JsonResponse({'message': 'Booking created successfully!'})
        except Venue.DoesNotExist:
            return JsonResponse({'error': 'Venue not found'}, status=404)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
from django.http import JsonResponse
from .models import Venue

def get_venues(request):
    venues = Venue.objects.all()
    data = []

    for venue in venues:
        data.append({
            'id': venue.id,
            'name': venue.name,
            'location': venue.location,
            'capacity': venue.capacity
        })

    return JsonResponse(data, safe=False)
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Feedback

@csrf_exempt
def submit_feedback(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        if not name or not email or not message:
            return JsonResponse({'error': 'Missing fields'}, status=400)

        Feedback.objects.create(name=name, email=email, message=message)

        return JsonResponse({'message': 'Feedback submitted successfully!'})

    return JsonResponse({'error': 'Invalid request method'}, status=400)
from django.http import JsonResponse
from .models import Booking

def get_bookings(request):
    venue_id = request.GET.get('venue_id')

    if not venue_id:
        return JsonResponse({'error': 'Venue ID is required'}, status=400)

    bookings = Booking.objects.filter(venue_id=venue_id).values('booked_by', 'date', 'approved')

    return JsonResponse(list(bookings), safe=False)