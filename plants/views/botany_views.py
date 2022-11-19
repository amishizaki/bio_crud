from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models.botany import Botany
from ..serializers import BotanySerializer, PlantCategorizedSerializer

# Create your views here.
#localhost:3000/botanys/ get post
class BotanyView(APIView):
    """View class for botanys/ for viewing all and creating"""
    serializer_class = BotanySerializer
    def get(self, request):
        botany = Botany.objects.all()
        serializer = PlantCategorizedSerializer(botany, many=True)
        return Response({'botany': serializer.data})

    def post(self, request):
        serializer = BotanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#localhost:3000/botany/:id get delete update
class BotanyDetailView(APIView):
    """View class for botany/:pk for viewing a single botany, updating a single botany, or removing a single botany"""
    serializer_class = BotanySerializer
    def get(self, request, pk):
        botany = get_object_or_404(Botany, pk=pk)
        serializer = PlantCategorizedSerializer(botany)
        return Response({'botany': serializer.data})

    def patch(self, request, pk):
        botany = get_object_or_404(Botany, pk=pk)
        serializer = BotanySerializer(botany, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        botany = get_object_or_404(Botany, pk=pk)
        botany.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
