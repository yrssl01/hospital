from rest_framework import viewsets
from rest_framework import mixins

from rest_framework.response import Response

from api.models import Doctor, Patient
from api.serializers.doctor import DoctorListSerializer, DoctorCreateSerializer, DoctorUpdateSerializer, DoctorRetrieveSerializer
from api.serializers.patient import PatientListSerializer
from api.mixin import HospitalGenericViewset
from django_filters.rest_framework import DjangoFilterBackend
from api.filters import DoctorFilterset


class DoctorView(
    HospitalGenericViewset,
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):

    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['first_name', 'last_name', 'specialization']
    filterset_class = DoctorFilterset

    def get_serializer_class(self):
        if (self.action == 'list'):
            return DoctorListSerializer
        if (self.action == 'retrieve'):
            return DoctorRetrieveSerializer
        if (self.action == 'create'):
            return DoctorCreateSerializer
        if (self.action == 'update'):
            return DoctorUpdateSerializer
        if (self.action == 'list_patient'):
            return PatientListSerializer

    def get_action_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_doctor', ]
        elif self.action == 'list_patient':
            self.action_permissions = ['view_patient', ]
        else:
            self.action_permissions = []

    def get_queryset(self):
        if self.action == 'list_patient':
            return Patient.objects.prefetch_related(
                'appointments'
            ).all()
        return Doctor.objects.all()

    def list_patient(self, request, pk):
        queryset = self.get_queryset().filter(appointments__doctor_id=pk)

        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data)