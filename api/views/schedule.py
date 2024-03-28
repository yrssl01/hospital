from api.mixin import HospitalGenericViewset
from rest_framework import mixins, filters
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Schedule
from api.serializers.schedule import ScheduleListSerializer, ScheduleDetailedSerializer, ScheduleCreateOrUpdateSerializer

class ScheduleView(
    HospitalGenericViewset,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    def get_serializer_class(self):
        if (self.action == 'list'):
            return ScheduleListSerializer
        if (self.action == 'retrieve'):
            return ScheduleDetailedSerializer
        if (self.action == 'create'):
            return ScheduleCreateOrUpdateSerializer
        if (self.action == 'update'):
            return ScheduleCreateOrUpdateSerializer

    def get_action_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_schedule', ]
        elif self.action == 'create':
            self.action_permissions = ['add_schedule', ]
        elif self.action == 'update':
            self.action_permissions = ['change_schedule', ]
        elif self.action == 'destroy':
            self.action_permissions = ['delete_schedule']
        else:
            self.action_permissions = []

    def get_queryset(self):
        return Schedule.objects.all()