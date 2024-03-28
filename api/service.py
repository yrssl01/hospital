import datetime

from .models import Appointment

def get_upcoming_appointments_count():
    return Appointment.objects.filter(
        schedule__timestamp_start__gte = datetime.datetime.now()
    ).count()