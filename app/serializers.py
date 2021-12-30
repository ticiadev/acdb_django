from rest_framework import serializers
from .models import villager

class villagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = villager
        fields = '__all__'