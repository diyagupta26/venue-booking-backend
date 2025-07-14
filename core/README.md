# Venue Booking System - Backend

A Django-based backend for managing venues, bookings, and feedback. The system supports RESTful APIs for:

- Venue listing
- Booking creation
- Feedback submission
- Admin approval

## Tech Stack
- Python
- Django
- SQLite
- Python `requests` for API testing

## How to Run
1. Clone the repo
2. Navigate to the folder:
cd venue_backend

markdown
Copy
Edit
3. Install dependencies (if needed)
4. Run the development server:
python manage.py runserver

markdown
Copy
Edit

## API Endpoints

- `POST /create-booking/` — Create a new booking
- `GET /get-bookings/` — View all bookings
- `POST /submit-feedback/` — Submit feedback