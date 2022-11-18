from django.urls import path 
from .views import PlantDetailView, PlantsView

urlpatterns = [
    path('', PlantsView.as_view(), name='plants'),
    path('<int:pk>/', PlantDetailView.as_view(), name='plant')
]