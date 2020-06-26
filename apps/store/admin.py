from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db import models

from apps.store.models import *


class ClotheInfoInline(admin.StackedInline):
    model = ClotheInfo
    readonly_fields = ['id']


class ImageInLine(admin.StackedInline):
    models = Image


@admin.register(Clothe)
class ClotheAdmin(ModelAdmin):
    list_display = ['id', 'code', 'price', 'discounted_price', 'is_discounted',
                    'category', 'kind']
    fields = ['id', 'created', 'modified', 'code', 'price',
              'discounted_price', 'is_discounted',
              'description', 'kind', 'category']
    readonly_fields = ['id', 'created', 'modified']
    inlines = [ClotheInfoInline, ImageInLine]


@admin.register(ClotheKind)
class ClotheKindAdmin(ModelAdmin):
    pass


@admin.register(ClotheSize)
class ClotheSizeAdmin(ModelAdmin):
    pass


@admin.register(ClotheColor)
class ClotheColorAdmin(ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass


@admin.register(Basket)
class BasketAdmin(ModelAdmin):
    pass


@admin.register(ProductInBasket)
class ProductInBasketAdmin(ModelAdmin):
    readonly_fields = ('total_price',)
    pass
