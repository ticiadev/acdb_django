from rest_framework import serializers
from .models import villagers

class villagersSerializer(serializers.ModelSerializer):

    class Meta:
        model = villagers
        fields = '__all__'