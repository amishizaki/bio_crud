from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models.plant import Plant
from ..serializers import PlantSerializer

# Create your views here.
#localhost:3000/plants/ get post
class PlantsView(APIView):
    """View class for plants/ for viewing all and creating"""
    serializer_class = PlantSerializer
    def get(self, request):
        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)
        return Response({'plants': serializer.data})

    def post(self, request):
        serializer = PlantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#localhost:3000/plants/:id get delete update
class PlantDetailView(APIView):
    """View class for plants/:pk for viewing a single plant, updating a single plant, or removing a single plant"""
    serializer_class = PlantSerializer
    def get(self, request, pk):
        plant = get_object_or_404(Plant, pk=pk)
        serializer = PlantSerializer(plant)
        return Response({'plant': serializer.data})

    def patch(self, request, pk):
        plant = get_object_or_404(Plant, pk=pk)
        serializer = PlantSerializer(plant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        plant = get_object_or_404(Plant, pk=pk)
        plant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
