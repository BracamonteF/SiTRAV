from rest_framework import serializers
from .models import Conductores, TiposCarnet, ConductoresCarnet

class ConductoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductores
        fields = '__all__'


class TiposCarnetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiposCarnet
        fields = '__all__'


class ConductoresCarnetSerializer(serializers.ModelSerializer):
    conductor = ConductoresSerializer()
    tipo_carnet = TiposCarnetSerializer()

    class Meta:
        model = ConductoresCarnet
        fields = '__all__'