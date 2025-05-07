from rest_framework import serializers
from .models import Fulfilment

class FulfilmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fulfilment
        fields = '__all__'
