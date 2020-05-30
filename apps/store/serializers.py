from rest_framework import serializers
from .models import *


class ClotheSizeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClotheSize
        exclude = ['id']


class ClotheColorSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClotheColor
        exclude = ['id']


class ClotheKindSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClotheKind
        exclude = ['id']


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['id']


class ClotheInfoSerializers(serializers.ModelSerializer):
    color = ClotheColorSerializers()
    size = ClotheSizeSerializers()

    class Meta:
        model = ClotheSize
        fields = ['count', 'color', 'size']


class ClotheSerializers(serializers.ModelSerializer):
    kind = ClotheKindSerializers()
    category = CategorySerializers()
    clothe_info = ClotheInfoSerializers(many=True)

    class Meta:
        model = Clothe
        fields = ['id', 'code', 'price', 'discounted_price', 'is_discounted',
                  'category', 'kind', 'description', 'clothe_info']
