from django.contrib import admin
from .models import Booking
from .models import APICallRecord

# Register your models here.

admin.site.register(Booking)
admin.site.register(APICallRecord)
