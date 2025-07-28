from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model
class CustomUser(AbstractUser):
    pass

# Venue Model
class Venue(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    image = models.ImageField(upload_to='venue_images/')

    def __str__(self):
        return self.name

# Booking Model
class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Who booked
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)      # What venue
    date = models.DateField()
    is_approved = models.BooleanField(default=False)                # Admin approval

    def __str__(self):
        return f"{self.user.username} - {self.venue.name} - {self.date}"