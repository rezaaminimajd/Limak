from rest_framework import serializers
from .models import *


class ClotheSizeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClotheSize
        fields = ['name']


class ClotheColorSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClotheColor
        fields = ['name']


class ClotheKindSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClotheKind
        fields = ['name']


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ClotheInfoSerializers(serializers.ModelSerializer):
    color = ClotheColorSerializers()
    size = ClotheSizeSerializers()

    class Meta:
        model = ClotheInfo
        fields = ['count', 'color', 'size']


class ClotheSerializers(serializers.ModelSerializer):
    kind = ClotheKindSerializers()
    category = CategorySerializers()
    information = ClotheInfoSerializers(many=True)

    class Meta:
        model = Clothe
        fields = ['id', 'code', 'price', 'discounted_price', 'is_discounted',
                  'category', 'kind', 'description', 'information']


class ClotheInBasketSerializer(serializers.ModelSerializer):
    kind = ClotheKindSerializers()
    category = CategorySerializers()

    class Meta:
        model = Clothe
        fields = ('id', 'code', 'price', 'discounted_price', 'is_discounted',
                  'category', 'kind', 'description')


class ProductInBasketSerializer(serializers.ModelSerializer):
    clothe = ClotheInBasketSerializer(read_only=True)
    color = ClotheColorSerializers(read_only=True)

    class Meta:
        model = ProductInBasket
        fields = ('clothe', 'count', 'color')


class BasketSerializer(serializers.ModelSerializer):
    products = ProductInBasketSerializer(many=True)

    class Meta:
        model = Basket
        fields = ('products', 'payed')
