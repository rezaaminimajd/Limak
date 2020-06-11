from django.db import models


class TransactionCreatorRequest(models.Model):
    pass


class Transaction(models.Model):
    id = models.CharField(max_length=512)
    link = models.CharField(max_length=512)


class TransactionInquiryResponse(models.Model):
    status = models.IntegerField()
    track_id = models.IntegerField()
    id = models.CharField(max_length=512)
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
