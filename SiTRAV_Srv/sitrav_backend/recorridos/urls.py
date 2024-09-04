from django.urls import path
from .views import RecorridosListCreate, PosicionesListCreate

urlpatterns = [
    path('recorridos/', RecorridosListCreate.as_view(), 
         name='recorridos-list-create'),
    path('posiciones/', PosicionesListCreate.as_view(), 
         name='posiciones-list-create'),
]