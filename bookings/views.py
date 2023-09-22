from django.shortcuts import render
from .get_bookings_lists_utils import get_bookings_lists
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index_bookings(request):
    bookingsResponse = get_bookings_lists()
    return render(request, "bookings/index.html", {
        'allBookings': bookingsResponse['allBookings'],
        'todayCheckInBookings': bookingsResponse['todayCheckInBookings'],
        'nextThreeDaysCheckoutBookings': bookingsResponse['nextThreeDaysCheckoutBookings'],
    })
