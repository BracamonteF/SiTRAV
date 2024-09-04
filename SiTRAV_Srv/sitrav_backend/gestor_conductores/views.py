from rest_framework import generics
from .models import Conductores
from .serializers import ConductoresSerializer

class ConductoresListCreate(generics.ListCreateAPIView):
    queryset = Conductores.objects.all()
    serializer_class = ConductoresSerializer