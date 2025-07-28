from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.name