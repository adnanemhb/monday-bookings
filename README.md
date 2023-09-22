# monday-bookings

This is a Django Python project for managing Monday bookings. Follow the steps below to get the project up and running.

Getting Started


Prerequisites
Before you begin, make sure you have the following installed on your system:

    Python 3.x
    Django
    Monday.com account (for API access)


Clone the Repository
    git clone https://github.com/adnanemhb/monday-booking.git

Navigate to the project directory and run the following commands to set up the database:
    cd monday-booking
    python manage.py makemigrations
    python manage.py migrate


Environment Variables
    Create a .env file in the project directory and add the following variables:

    API_ENDPOINT=YOUR_MONDAY_API_URL
    API_TOKEN=YOUR_BEARER_TOKEN


Running the Application

    To start the Django development server, run the following command:
    
    python manage.py runserver


Your Monday booking project should now be running locally. You can access it in your web browser at http://127.0.0.1:8000.
