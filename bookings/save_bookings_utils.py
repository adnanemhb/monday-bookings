from .models import Booking


def save_bookings_to_database(bookings):
    saved_bookings = []

    for booking_data in bookings:
        item_id = booking_data['item_id']

        existing_booking = Booking.objects.filter(item_id=item_id).first()

        if existing_booking:
            saved_bookings.append(existing_booking)
        else:
            booking = Booking(
                guest_name=booking_data['guest_name'],
                status=booking_data['status'],
                flat_booked=booking_data['flat_booked'],
                check_in_date=booking_data['check_in_date'] if booking_data['check_in_date'] != '' else None,
                check_out_date=booking_data['check_out_date'],
                creation_log=booking_data['creation_log'],
                booking_value=booking_data['booking_value'],
                item_id=item_id,
            )
            booking.save()
            saved_bookings.append(booking)

    return saved_bookings
