from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from api.models import Appointment, Schedule

class AppointmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentCreateSerializer(serializers.ModelSerializer):

    def validate_schedule(self, value):
        appointment_count = value.appointments.count()
        if 3 <= appointment_count:
            raise ValidationError("Превышено максимальное количество мест!")
        return value

    class Meta:
        model = Appointment
        fields = ['patient', 'service', 'schedule']


class AppointmentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['status']


class AppointmentRatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=0, max_value=10)

    def validate_rating(self, value):
        if self.instance.rating_set:
            raise ValidationError("Вы уже ставили рейтинг!")

    class Meta:
        model = Appointment
        fields = ['rating']