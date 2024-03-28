from rest_framework.response import Response
from rest_framework import status
from api.mixin import HospitalGenericViewset
from api.models import Doctor, Patient

from api.service import get_upcoming_appointments_count


class AnalyticsView(
    HospitalGenericViewset
):

    def get_action_permissions(self):
        if self.action == 'get_analytics':
            self.action_permissions = []

    def get_analytics(self, req):
        response = {
            'patient_count': Patient.objects.all().count(),
            'doctor_count': Doctor.objects.all().count(),
            'appointment_count': get_upcoming_appointments_count()
        }
        return Response(status=status.HTTP_200_OK, data=response)