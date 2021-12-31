from rest_framework import serializers
from .models import Villager, Personality, Coffee, Game, Amiibo, House, \
    Furniture


class VillagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Villager
        fields = '__all__'


class PersonalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Personality
        fields = '__all__'


class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class AmiiboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amiibo
        fields = '__all__'


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'


class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = '__all__'
