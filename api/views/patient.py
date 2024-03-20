from api.mixin import HospitalGenericViewset
from rest_framework import mixins, filters
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Patient
from api.serializers.patient import PatientListSerializer, PatientDetailedSerializer, PatientCreateOrUpdateSerializer

class PatientView(
    HospitalGenericViewset,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['gender']
    search_fields = ['first_name', 'last_name']

    def get_serializer_class(self):
        if (self.action == 'list'):
            return PatientListSerializer
        if (self.action == 'retrieve'):
            return PatientDetailedSerializer
        if (self.action == 'create'):
            return PatientCreateOrUpdateSerializer
        if (self.action == 'update'):
            return PatientCreateOrUpdateSerializer


    def get_action_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_patient', ]
        elif self.action == 'create':
            self.action_permissions = ['add_patient', ]
        elif self.action == 'update':
            self.action_permissions = ['change_patient', ]
        elif self.action == 'destroy':
            self.action_permissions = ['delete_patient']
        else:
            self.action_permissions = []

    def get_queryset(self):
        return Patient.objects.all()
