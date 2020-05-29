from django.contrib import admin

from .models import Profile, ResetPasswordToken


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(ResetPasswordToken)
class ResetPasswordTokenAdmin(admin.ModelAdmin):
    pass
