from django.shortcuts import redirect, render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Appointment
from api.permissions import AppointmentAccessPermission
from api.serializers.appointment import AppointmentCreateSerializer, AppointmentListSerializer, AppointmentUpdateSerializer, AppointmentRetrieveSerializer


class AppointmentView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):

    def get_serializer_class(self):
        if self.action == 'list':
            return AppointmentListSerializer
        if self.action == 'retrieve':
            return AppointmentRetrieveSerializer
        if self.action == 'create':
            return AppointmentCreateSerializer
        if self.action == 'update':
            return AppointmentUpdateSerializer

    permission_classes = [IsAuthenticated, AppointmentAccessPermission]

    def get_queryset(self):
        return Appointment.objects.all()