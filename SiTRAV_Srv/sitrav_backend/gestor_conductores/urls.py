from django.urls import path
from .views import ConductoresListCreateView, ConductoresDetailView, TiposCarnetListCreateView, TiposCarnetDetailView, ConductoresCarnetListCreateView, ConductoresCarnetDetailView

urlpatterns = [
    # Rutas para Conductores
    path('conductores/', ConductoresListCreateView.as_view(), name='conductores-list'),
    path('conductores/<int:pk>/', ConductoresDetailView.as_view(), name='conductores-detail'),

    # Rutas para TiposCarnet
    path('tipos_carnet/', TiposCarnetListCreateView.as_view(), name='tipos_carnet-list'),
    path('tipos_carnet/<int:pk>/', TiposCarnetDetailView.as_view(), name='tipos_carnet-detail'),

    # Rutas para ConductoresCarnet
    path('conductores_carnet/', ConductoresCarnetListCreateView.as_view(), name='conductores_carnet-list'),
    path('conductores_carnet/<int:pk>/', ConductoresCarnetDetailView.as_view(), name='conductores_carnet-detail'),
]