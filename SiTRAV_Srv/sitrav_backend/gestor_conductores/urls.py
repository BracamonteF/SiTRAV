from django.urls import path
from .views import ConductoresListCreate

urlpatterns = [
    path('conductores/', ConductoresListCreate.as_view(), 
         name='conductores-list-create'),
]
