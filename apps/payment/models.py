from django.db import models
from model_utils.models import TimeStampedModel, UUIDModel
from .services.inquiry_payment import InquiryPayment


class TransactionStatusTypes:
    NOT_PAYED = 1
    PAYMENT_UNSUCCESSFUL = 2
    ERROR = 3
    MONEY_BLOCKED = 4
    RETURN_PAYER = 5
    SYSTEMIC_RETURNED = 6
    CANCELED_PAYMENT = 7
    TRANSFERRED_TO_PAYMENT_PAGE = 8
    WAITING_FOR_PAYMENT_VERIFICATION = 10
    PAYMENT_VERIFIED = 100
    PAYMENT_VERIFIED_PREVIOUSLY = 101
    TRANSFERRED_COMPLETELY = 200

    TYPES = (
        (NOT_PAYED, 'پرداخت انجام نشده است'),
        (PAYMENT_UNSUCCESSFUL, 'پرداخت ناموفق بوده است'),
        (ERROR, 'خطا رخ داده است'),
        (MONEY_BLOCKED, 'بلوکه شده'),
        (RETURN_PAYER, 'برگشت به پرداخت کننده'),
        (SYSTEMIC_RETURNED, 'برگشت خورده سیستمی'),
        (CANCELED_PAYMENT, 'انصراف از پرداخت'),
        (TRANSFERRED_TO_PAYMENT_PAGE, 'به درگاه پرداخت منتقل شد'),
        (WAITING_FOR_PAYMENT_VERIFICATION, 'در انتظار تایید پرداخت'),
        (PAYMENT_VERIFIED, 'پرداخت تایید شده است'),
        (PAYMENT_VERIFIED_PREVIOUSLY, 'پرداخت قبلا تایید شده است'),
        (TRANSFERRED_COMPLETELY, 'به دریافت کننده واریز شد')
    )

    TYPES_DICT = dict(TYPES)


class TransactionCreatorRequest(models.Model):
    pass


class Transaction(UUIDModel, TimeStampedModel):
    id_pay_id = models.CharField(max_length=512, unique=True)
    link = models.CharField(max_length=512)
    order = models.ForeignKey('store.Basket', related_name='transactions',
                              on_delete=models.DO_NOTHING)
    amount = models.IntegerField()
    name = models.CharField(max_length=256, blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    mail = models.CharField(max_length=64, blank=True, null=True)
    desc = models.CharField(max_length=256, blank=True, null=True)

    @property
    def payed(self):
        return self.callbacks.all().last().status in (
            TransactionStatusTypes.PAYMENT_VERIFIED,
            TransactionStatusTypes.PAYMENT_VERIFIED_PREVIOUSLY,
            TransactionStatusTypes.TRANSFERRED_COMPLETELY

        )

    errors = models.TextField(default='')

    class Meta:
        constraints = (
            models.UniqueConstraint(fields=('id_pay_id', 'order'),
                                    name='unique_order'),
        )


class TransactionCallback(UUIDModel, TimeStampedModel):
    transaction = models.ForeignKey(Transaction,
                                    related_name='callbacks',
                                    on_delete=models.CASCADE,
                                    blank=True,
                                    null=True)
    status = models.PositiveSmallIntegerField(
        choices=TransactionStatusTypes.TYPES
    )
    track_id = models.IntegerField()
    id_pay_id = models.CharField(max_length=512)
    order_id = models.CharField(max_length=128)
    amount = models.IntegerField()
    card_no = models.CharField(max_length=128)
    hashed_card_no = models.CharField(max_length=512)
    date = models.DateTimeField()
    errors = models.TextField(default='')


class TransactionInquiryResponse(models.Model):
    status = models.IntegerField(null=True, blank=True)
    track_id = models.IntegerField(null=True, blank=True)
    id_pay_id = models.CharField(max_length=512, null=True, blank=True)
    order_id = models.CharField(max_length=512, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        transaction_inquiry_response = InquiryPayment(
            self.id_pay_id,
            self.order_id
        ).complete_fields()
        super(TransactionInquiryResponse, self).save(
            transaction_inquiry_response
        )


class Wage(models.Model):
    transaction_inquiry_response = models.ForeignKey(
        'payment.TransactionInquiryResponse', on_delete=models.CASCADE,
        related_name='wage')
    by = models.CharField(max_length=32, null=True, blank=True)
    type = models.CharField(max_length=32, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)


class Payer(models.Model):
    transaction_inquiry_response = models.ForeignKey(
        'payment.TransactionInquiryResponse', on_delete=models.CASCADE,
        related_name='payer')
    name = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=128, null=True, blank=True)
    mail = models.CharField(max_length=128, null=True, blank=True)
    desc = models.CharField(max_length=1024, null=True, blank=True)


class Payment(models.Model):
    transaction_inquiry_response = models.ForeignKey(
        'payment.TransactionInquiryResponse', on_delete=models.CASCADE,
        related_name='payment')
    track_id = models.IntegerField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    card_no = models.CharField(max_length=1024, null=True, blank=True)
    hashed_card_no = models.CharField(max_length=1024, null=True, blank=True)
    date = models.IntegerField(null=True, blank=True)


class Verify(models.Model):
    transaction_inquiry_response = models.ForeignKey(
        'payment.TransactionInquiryResponse', on_delete=models.CASCADE,
        related_name='verify')
    date = models.IntegerField(null=True, blank=True)

    class Settlement(models.Model):
        transaction_inquiry_response = models.ForeignKey(
            'payment.TransactionInquiryResponse', on_delete=models.CASCADE,
            related_name='settlement')
        track_id = models.IntegerField(null=True, blank=True)
        amount = models.IntegerField(null=True, blank=True)
        date = models.IntegerField(null=True, blank=True)
