from django.urls import path
from .views import VehiculosListCreate, VehiculosMotoresListCreate, MotoresListCreate

urlpatterns = [
    path('vehiculos/', VehiculosListCreate.as_view(), 
         name='vehiculos-list-create'),
    path('instalaciones_motores/', VehiculosMotoresListCreate.as_view(), 
         name='instalaciones-list-create'),
    path('motores/', MotoresListCreate.as_view(), 
         name='motores-list-create'),
]