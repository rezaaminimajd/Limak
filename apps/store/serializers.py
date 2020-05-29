from rest_framework import serializers
from .models import Clothe


class ClotheSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clothe
        fields = ['__all__']


