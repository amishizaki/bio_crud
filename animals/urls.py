from django.urls import path 
from .views import AnimalDetailView, AnimalsView

urlpatterns = [
    path('', AnimalsView.as_view(), name='animals'),
    path('<int:pk>/', PlantDetailView.as_view(), name='animal')
]