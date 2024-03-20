from django.shortcuts import redirect, render
from rest_framework import viewsets
from rest_framework import mixins

from api.models import Service
from api.serializers.service import ServiceListSerializer, ServiceUpdateSerializer, ServiceCreateSerializer, ServiceRetrieveSerializer


class ServiceView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):

    def get_serializer_class(self):
        if self.action == 'list':
            return ServiceListSerializer
        if self.action == 'retrieve':
            return ServiceRetrieveSerializer
        if self.action == 'create':
            return ServiceCreateSerializer
        if self.action == 'update':
            return ServiceUpdateSerializer

    def get_queryset(self):
        return Service.objects.all()