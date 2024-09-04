from rest_framework import serializers
from .models import Vehiculos
from .models import Motores
from .models import VehiculosMotores


class VehiculosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculos
        fields = '__all__'

class VehiculosMotoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiculosMotores
        fields = '__all__'

class MotoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motores
        fields = '__all__'