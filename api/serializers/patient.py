from rest_framework import serializers
from api.models import Patient

class PatientListSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    date_of_birth = serializers.DateField()
    gender = serializers.CharField()


class PatientDetailedSerializer(PatientListSerializer):
    contact_info = serializers.CharField()


class PatientCreateOrUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
