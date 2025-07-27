from django.contrib import admin
from .models import CustomUser, Venue  # Import both together

# ✅ Register each model only once
admin.site.register(CustomUser)
admin.site.register(Venue)