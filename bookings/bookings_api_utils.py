import requests
from decouple import config
from bookings.models import APICallRecord
from django.utils import timezone

from .bookings_formatting_utils import format_bookings
from .save_bookings_utils import save_bookings_to_database


def get_and_save_bookings_with_api():
    API_ENDPOINT = config('API_ENDPOINT')
    API_TOKEN = config('API_TOKEN')
    if API_TOKEN is None or API_ENDPOINT is None:
        return {
            'status': False,
            'bookings': {},
            'message': 'Check your API credentials'
        }

    headers = {
        "Authorization": "Bearer " + API_TOKEN,
        "Content-Type": "application/json",
    }

    request_data = {
        "query": "query { boards (workspace_ids: 85401) {id name  items { id name group { title id } state created_at "
                 "column_values"
                 "{title value text additional_info }} } }"
    }

    try:
        response = requests.post(API_ENDPOINT, headers=headers, json=request_data)
        if response.status_code == 200:
            bookings_data = response.json()

            if 'errors' in bookings_data:
                return {
                    'status': False,
                    'bookings': {},
                    'message': 'API returned errors: ' + str(bookings_data['errors'])
                }
            booking_data = bookings_data.get('data', {})
            formattedData = format_bookings(booking_data['boards'])
            save_bookings_to_database(formattedData)
            save_api_call_record()
            return {
                'status': True,
                'bookings': {},
                'message': ''
            }
        else:
            return {
                'status': False,
                'bookings': {},
                'message': f"Request failed with status code {response.status_code}"
            }
    except requests.exceptions.RequestException as e:
        return {
            'status': False,
            'bookings': {},
            'message': f"Request Exception: {str(e)}"
        }


def save_api_call_record():
    current_time = timezone.now()
    record, created = APICallRecord.objects.get_or_create(pk=1)

    if created or (current_time - record.last_api_call).total_seconds() > 1800:
        record.last_api_call = current_time
        record.save()