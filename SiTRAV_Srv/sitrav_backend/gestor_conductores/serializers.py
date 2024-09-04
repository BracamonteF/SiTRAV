from rest_framework import serializers
from .models import Conductores

class ConductoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductores
        fields = '__all__'