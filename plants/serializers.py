from rest_framework import serializers

from .models.plant import Plant
from .models.field import Field

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Plant

class PlantSortSerializer(serializers.ModelSerializer):
    field = serializers.StringRelatedField()
    class Meta:
        fields = '__all__'
        model = Plant

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Field