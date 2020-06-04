from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db import models

from apps.store.models import *


class ClotheInfoInline(admin.StackedInline):
    model = ClotheInfo
    readonly_fields = ['id']


@admin.register(Clothe)
class ClotheAdmin(ModelAdmin):
    list_display = ['code', 'price', 'discounted_price', 'is_discounted',
                    'category', 'kind']
    inlines = [ClotheInfoInline]


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
