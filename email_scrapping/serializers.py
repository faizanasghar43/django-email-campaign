from .models import Scrappy
from rest_framework import serializers


class ScrappingSerializer(serializers.ModelSerializer):
    emails = serializers.ListField(child=serializers.CharField())
    class Meta:
        model = Scrappy
        fields = ['url', 'emails', 'user']
