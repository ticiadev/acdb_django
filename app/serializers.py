from rest_framework import serializers
from .models import Villager

class VillagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Villager
        fields = '__all__'