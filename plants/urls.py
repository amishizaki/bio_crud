from django.urls import path 
from .views.plant_views import PlantDetailView, PlantsView
from .views.botany_views import BotanyDetailView, BotanyView

urlpatterns = [
    path('', PlantsView.as_view(), name='plants'),
    path('<int:pk>/', PlantDetailView.as_view(), name='plant'),
    path('', BotanyView.as_view(), name='botany'),
    path('<int:pk>/', BotanyDetailView.as_view(), name='botany'),
]