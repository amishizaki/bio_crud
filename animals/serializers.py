from rest_framework import serializers

from .models.animal import Animal

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Animal