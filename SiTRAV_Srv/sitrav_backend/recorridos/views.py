from rest_framework import generics
from .models import Recorridos, Posiciones
from .serializers import PosicionesSerializer, RecorridosSerializer

class RecorridosListCreate(generics.ListCreateAPIView):
    queryset = Recorridos.objects.all()
    serializer_class = RecorridosSerializer

class PosicionesListCreate(generics.ListCreateAPIView):
    queryset = Posiciones.objects.all()
    serializer_class = PosicionesSerializer