from rest_framework import serializers
from rest_framework.generics import get_object_or_404

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
    size = ClotheSizeSerializers(read_only=True)
    clothe_uid = serializers.CharField(max_length=200)
    color_name = serializers.CharField(max_length=100)
    size_name = serializers.CharField(max_length=100)

    class Meta:
        model = ProductInBasket
        fields = ('clothe', 'count', 'color', 'size',
                  'clothe_uid', 'color_name', 'size_name')
        extra_kwargs = {
            'cloth': {'read_only': True},
            'color': {'read_only': True},
            'size': {'read_only': True},
            'clothe_uid': {'write_only': True},
            'color_name': {'write_only': True},
            'size_name': {'write_only': True}
        }

    def validate(self, attrs):
        attrs['clothe'] = get_object_or_404(Clothe,
                                            id=attrs.get('clothe_uid'))
        attrs['color'] = get_object_or_404(ClotheColor,
                                           name=attrs.get('color_name'))
        attrs['size'] = get_object_or_404(ClotheSize,
                                          name=attrs.get('size_name'))
        basket = Basket.objects.filter(user=self.context['request'].user
                                       ).filter(payed=False).last()
        if not basket:
            basket = Basket.objects.create(user=self.context['request'].user)
        attrs['basket'] = basket

    def create(self, validated_data):
        return ProductInBasket.objects.create(**validated_data)


class BasketSerializer(serializers.ModelSerializer):
    products = ProductInBasketSerializer(many=True)

    class Meta:
        model = Basket
        fields = ('products', 'payed')
