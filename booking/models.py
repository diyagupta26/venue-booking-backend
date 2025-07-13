from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    booked_by = models.CharField(max_length=100)
    date = models.DateField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.booked_by} - {self.venue.name}"

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.email})"
