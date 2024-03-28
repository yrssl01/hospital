from django.shortcuts import redirect, render
from rest_framework import viewsets, status
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Appointment
from api.permissions import AppointmentAccessPermission
from api.serializers.appointment import AppointmentCreateSerializer, AppointmentListSerializer, AppointmentUpdateSerializer, AppointmentRetrieveSerializer, AppointmentRatingSerializer


class AppointmentView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):

    def get_action_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_appointment', ]
        elif self.action == 'create':
            self.action_permissions = ['add_appointment', ]
        # elif self.action == 'update':
        #     self.action_permissions = ['change_appointment', ]
        # elif self.action == 'destroy':
        #     self.action_permissions = ['delete_appointment', ]
        else:
            self.action_permissions = []


    def get_serializer_class(self):
        if self.action == 'list':
            return AppointmentListSerializer
        if self.action == 'retrieve':
            return AppointmentRetrieveSerializer
        if self.action == 'create':
            return AppointmentCreateSerializer
        if self.action == 'update':
            return AppointmentUpdateSerializer
        if self.action == 'set_rating':
            return AppointmentRatingSerializer

    permission_classes = [IsAuthenticated, AppointmentAccessPermission]

    def get_queryset(self):
        return Appointment.objects.all()


    def set_rating(self, req, pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_200_OK)