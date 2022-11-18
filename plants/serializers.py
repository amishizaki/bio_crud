from rest_framework import serializers

from .models import Plant

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Plant