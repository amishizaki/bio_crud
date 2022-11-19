from rest_framework import serializers

from .models.plant import Plant

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Plant