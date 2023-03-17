from rest_framework import serializers

from .models import Aspirant, Technologies


class AspirantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aspirant
        fields = '__all__'


class TechnologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technologies
        fields = '__all__'