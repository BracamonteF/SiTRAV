from rest_framework import serializers
from .models import Posiciones
from .models import Recorridos

class PosicionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posiciones
        fields = '__all__'

class RecorridosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recorridos
        fields = '__all__'