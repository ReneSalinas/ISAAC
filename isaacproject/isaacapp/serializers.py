from rest_framework import serializers
from .models import ActiveItem

class ActiveItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveItem
        fields = '__all__'