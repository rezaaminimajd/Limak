from django.db import models


class TransactionStatusTypes:
    NOT_PAYED = 1
    PAYMENT_UNSUCCESSFUL = 2
    ERROR = 3
    MONEY_BLOCKED = 4
    RETURN_PAYER = 5
    SYSTEMIC_RETURNED = 6
    CANCELED_PAYMENT = 7
    TRANSFERRED_TO_PAYMENT_PAGE = 8
    WAITING_FOR_PAYMENT_CONFIRMATION = 10
    PAYMENT_CONFIRMED = 100
    PAYMENT_CONFIRMED_PREVIOUSLY = 101
    TRANSFERRED_COMPLETELY = 200


class TransactionCreatorRequest(models.Model):
    pass


class Transaction(models.Model):
    id_pay_id = models.CharField(max_length=512, unique=True)
    link = models.CharField(max_length=512)
    order = models.ForeignKey('store.Basket', related_name='transactions',
                              on_delete=models.DO_NOTHING)
    amount = models.IntegerField()
    name = models.CharField(max_length=256, blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    mail = models.CharField(max_length=64, blank=True, null=True)
    desc = models.CharField(max_length=256, blank=True, null=True)

    errors = models.TextField(default='')

    class Meta:
        constraints = (
            models.UniqueConstraint(fields=('id_pay_id', 'order'),
                                    name='unique_order'),
        )


class TransactionInquiryResponse(models.Model):
    status = models.IntegerField()
    track_id = models.IntegerField()
    id_pay_id = models.CharField(max_length=512)
    order_id = models.CharField(max_length=512)
    amount = models.IntegerField()


class Wage(models.Model):
    transaction_inquiry_response = models.ForeignKey(
        'payment.TransactionInquiryResponse', on_delete=models.CASCADE,
        related_name='wage')
    by = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    amount = models.IntegerField()


class Payer(models.Model):
    transaction_inquiry_response = models.ForeignKey(
        'payment.TransactionInquiryResponse', on_delete=models.CASCADE,
        related_name='payer')
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    mail = models.CharField(max_length=128)
    desc = models.CharField(max_length=1024)


class Payment(models.Model):
    transaction_inquiry_response = models.ForeignKey(
        'payment.TransactionInquiryResponse', on_delete=models.CASCADE,
        related_name='payment')
    track_id = models.IntegerField()
    amount = models.IntegerField()
    card_no = models.CharField(max_length=1024)
    hashed_card_no = models.CharField(max_length=1024)
    date = models.IntegerField()


class Verify(models.Model):
    transaction_inquiry_response = models.ForeignKey(
        'payment.TransactionInquiryResponse', on_delete=models.CASCADE,
        related_name='verify')
    date = models.IntegerField()


class Settlement(models.Model):
    transaction_inquiry_response = models.ForeignKey(
        'payment.TransactionInquiryResponse', on_delete=models.CASCADE,
        related_name='settlement')
    track_id = models.IntegerField()
    amount = models.IntegerField()
    date = models.IntegerField()
