from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models.field import Field
from ..serializers import FieldSerializer

# Create your views here.
#localhost:3000/fields/ get post
class FieldsView(APIView):
    """View class for fields/ for viewing all and creating"""
    serializer_class = FieldSerializer
    def get(self, request):
        fields = Field.objects.all()
        serializer = FieldSerializer(fields, many=True)
        return Response({'fields': serializer.data})

    def post(self, request):
        serializer = FieldSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#localhost:3000/fields/:id get delete update
class FieldDetailView(APIView):
    """View class for fields/:pk for viewing a single field, updating a single field, or removing a single field"""
    serializer_class = FieldSerializer
    def get(self, request, pk):
        field = get_object_or_404(Field, pk=pk)
        serializer = FieldSerializer(field)
        return Response({'field': serializer.data})

    def patch(self, request, pk):
        field = get_object_or_404(Field, pk=pk)
        serializer = FieldSerializer(field, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        field = get_object_or_404(Field, pk=pk)
        field.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
