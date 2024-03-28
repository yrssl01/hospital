from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from api.models import Schedule


class ScheduleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class ScheduleDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class ScheduleCreateOrUpdateSerializer(serializers.ModelSerializer):

    def validators(self, attrs):
        attrs = super().validate(attrs)

        timestamp_start, timestamp_end = attrs['timestamp_start'], attrs['timestamp_end']

        exists = Schedule.objects.filter(
            timestamp_start__lte=timestamp_start,
            timestamp_end__gte=timestamp_start
        ).exists()

        if exists:
            raise ValidationError("У нас есть накладка!")

    class Meta:
        model = Schedule
        fields = '__all__'