import json
from datetime import datetime


def format_bookings(bookings):
    bookingsToSave = []
    for board_data in bookings:
        for item_data in board_data['items']:
            check_in_date = ''
            check_out_date = ''
            flat_booked = ''
            booking_value = 0.0
            status = ''
            for column_value in item_data['column_values']:
                if column_value['title'] == 'Timeline' and is_valid_json(column_value['value']):
                    time_line_dict = json.loads(column_value['value'])
                    if 'start' in time_line_dict:
                        check_in_date = time_line_dict['from']
                    if 'to' in time_line_dict:
                        check_out_date = time_line_dict['to']
                elif column_value['title'] == 'Flat Booked':
                    flat_booked = column_value['value']
                elif column_value['title'] == 'Status' and column_value['value'] != '':
                    status = column_value['text']
                elif column_value['title'] == 'Booking Value' or column_value['title'] == 'Amount':
                    booking_value_Value = column_value['value']
                    if is_valid_float_string(booking_value_Value):
                        booking_value = float(booking_value_Value)
            booking = {
                'item_id': item_data['id'],
                'check_in_date': check_in_date,
                'check_out_date': check_out_date,
                'flat_booked': flat_booked,
                'booking_value': booking_value,
                'guest_name': item_data['name'],
                'status': status if status != '' else item_data['group']['title'] if item_data[
                    'group'] else 'empty_group',
                'creation_log': datetime.strptime(item_data['created_at'], '%Y-%m-%dT%H:%M:%SZ').strftime(
                    '%Y-%m-%d %H:%M'),
            }
            if check_out_date != '':
                bookingsToSave.append(booking)
    return bookingsToSave


def is_valid_json(my_string):
    if my_string is None or my_string == '':
        return False
    try:
        json.loads(my_string)
        return True
    except json.JSONDecodeError:
        return False


def is_valid_float_string(s):
    try:
        float_value = float(s)
        return True
    except (ValueError, TypeError):
        return False
