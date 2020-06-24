from django.contrib import admin
from .models import *


class WageInline(admin.StackedInline):
    model = Wage
    readonly_fields = ['by', 'type', 'amount']


class PayerInline(admin.StackedInline):
    model = Payer
    readonly_fields = ['name', 'phone', 'mail', 'desc']


class PaymentInline(admin.StackedInline):
    model = Payment
    readonly_fields = ['track_id', 'amount', 'card_no', 'hashed_card_no',
                       'date']


class VerifyInline(admin.StackedInline):
    model = Verify
    readonly_fields = ['date']


class SettlementInline(admin.StackedInline):
    model = Settlement
    readonly_fields = ['date', 'amount', 'track_id']


@admin.register(TransactionInquiryResponse)
class TransactionInquiryResponseAdmin(admin.ModelAdmin):
    list_display = ['id_pay_id', 'track_id']
    list_display_links = ['id_pay_id']
    readonly_fields = ['status', 'order_id', 'amount', 'date']
    inlines = [WageInline, PayerInline, VerifyInline, PaymentInline]


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass


@admin.register(TransactionCallback)
class TransactionCallbackAdmin(admin.ModelAdmin):
    pass
