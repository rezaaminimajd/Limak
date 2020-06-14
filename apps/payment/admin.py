from django.contrib import admin
from .models import TransactionInquiryResponse


@admin.register(TransactionInquiryResponse)
class TransactionInquiryResponseAdmin(admin.ModelAdmin):
    pass
