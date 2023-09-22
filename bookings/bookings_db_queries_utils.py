from .models import Booking
from datetime import date, timedelta


def get_all_bookings():
    return Booking.objects.all()


def get_today_checkin_bookings():
    today = date.today()
    return Booking.objects.filter(check_in_date=today)


def get_next_3_days_checkout_bookings():
    today = date.today()
    three_days_later = today + timedelta(days=3)
    return Booking.objects.filter(check_out_date__gte=today, check_out_date__lte=three_days_later)
