from rest_framework import serializers
from .models import Coffee


class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = ("id", "name", "size", "cup_size", "espresso", "total_mgs")
