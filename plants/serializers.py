from rest_framework import serializers

from .models.plant import Plant
from .models.botany import Botany

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Plant

class PlantCategorizedSerializer(serializers.ModelSerializer):
    botany = serializers.StringRelatedField()
    class Meta:
        fields = '__all__'
        model = Plant

class BotanySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Botany
