from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db import models

from apps.store.models import Clothe


@admin.register(Clothe)
class ClotheAdmin(ModelAdmin):
    pass


