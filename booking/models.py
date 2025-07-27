from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Agar tum future mein aur fields add karna chahti ho
    pass
from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name
    
    from django.db import models
from django.conf import settings

from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    image = models.ImageField(upload_to='venue_images/')  # Pillow is installed ✅

    def __str__(self):
        return self.name