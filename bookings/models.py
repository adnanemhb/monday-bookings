from django.db import models
from django.utils import timezone


class Booking(models.Model):
    guest_name = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=20, null=True)
    flat_booked = models.CharField(max_length=255, null=True)
    check_in_date = models.DateField(null=True, blank=True)
    check_out_date = models.DateField(null=True, blank=True)
    creation_log = models.DateTimeField(null=True)
    booking_value = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    item_id = models.BigIntegerField(null=True)

    def __str__(self):
        return f'{self.guest_name} - {self.flat_booked} - {self.check_in_date} to {self.check_out_date}'


class APICallRecord(models.Model):
    last_api_call = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Last API Call: {self.last_api_call}'
