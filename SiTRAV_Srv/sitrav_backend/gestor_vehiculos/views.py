from rest_framework import generics
from .models import VehiculosMotores, Vehiculos, Motores
from .serializers import VehiculosMotoresSerializer, VehiculosSerializer, MotoresSerializer

class MotoresListCreate(generics.ListCreateAPIView):
    queryset = Motores.objects.all()
    serializer_class = MotoresSerializer

class VehiculosMotoresListCreate(generics.ListCreateAPIView):
    queryset = VehiculosMotores.objects.all()
    serializer_class = VehiculosMotoresSerializer

class VehiculosListCreate(generics.ListCreateAPIView):
    queryset = Vehiculos.objects.all()
    serializer_class = VehiculosSerializer