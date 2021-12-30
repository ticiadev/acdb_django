from rest_framework import serializers
from .models import Villager, Personality

class VillagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Villager
        fields = '__all__'

class PersonalitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Personality
        fields = '__all__'
