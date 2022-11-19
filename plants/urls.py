from django.urls import path 
from .views.plant_views import PlantDetailView, PlantsView
from .views.field_views import FieldDetailView, FieldsView

urlpatterns = [
    path('plants/', PlantsView.as_view(), name='plants'),
    path('plants/<int:pk>/', PlantDetailView.as_view(), name='plant'),
    path('fields/', FieldsView.as_view(), name='fields'),
    path('fields/<int:pk>/', FieldDetailView.as_view(), name='field'),
]