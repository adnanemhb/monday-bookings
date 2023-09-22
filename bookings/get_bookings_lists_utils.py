from bookings.models import APICallRecord
from django.utils import timezone
from .bookings_db_queries_utils import get_all_bookings, get_today_checkin_bookings, get_next_3_days_checkout_bookings
from .bookings_api_utils import get_and_save_bookings_with_api


def get_bookings_lists():
    record = APICallRecord.objects.first()
    current_time = timezone.now()

    # Api call isn't done yet, or it was done before more that 30min: in this case I should call the api and save the
    # records
    if not record or (current_time - record.last_api_call).total_seconds() > 1800:
        get_and_save_bookings_with_api()
    return {
        'allBookings': get_all_bookings(),
        'todayCheckInBookings': get_today_checkin_bookings(),
        'nextThreeDaysCheckoutBookings': get_next_3_days_checkout_bookings(),
    }
