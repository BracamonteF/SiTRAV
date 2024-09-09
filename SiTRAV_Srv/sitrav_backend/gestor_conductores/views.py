from rest_framework import generics
from .models import Conductores, TiposCarnet, ConductoresCarnet
from .serializers import ConductoresSerializer, TiposCarnetSerializer, ConductoresCarnetSerializer


# Views para Conductores
class ConductoresListCreateView(generics.ListCreateAPIView):
    queryset = Conductores.objects.all()
    serializer_class = ConductoresSerializer


class ConductoresDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Conductores.objects.all()
    serializer_class = ConductoresSerializer


# Views para TiposCarnet
class TiposCarnetListCreateView(generics.ListCreateAPIView):
    queryset = TiposCarnet.objects.all()
    serializer_class = TiposCarnetSerializer


class TiposCarnetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TiposCarnet.objects.all()
    serializer_class = TiposCarnetSerializer


# Views para ConductoresCarnet
class ConductoresCarnetListCreateView(generics.ListCreateAPIView):
    queryset = ConductoresCarnet.objects.all()
    serializer_class = ConductoresCarnetSerializer


class ConductoresCarnetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConductoresCarnet.objects.all()
    serializer_class = ConductoresCarnetSerializer