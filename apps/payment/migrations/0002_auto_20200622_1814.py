# Generated by Django 3.0.6 on 2020-06-22 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactioninquiryresponse',
            name='date',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payer',
            name='transaction_inquiry_response',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payer', to='payment.TransactionInquiryResponse'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='transaction_inquiry_response',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='payment.TransactionInquiryResponse'),
        ),
        migrations.AlterField(
            model_name='settlement',
            name='transaction_inquiry_response',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='settlement', to='payment.TransactionInquiryResponse'),
        ),
        migrations.AlterField(
            model_name='verify',
            name='transaction_inquiry_response',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='verify', to='payment.TransactionInquiryResponse'),
        ),
        migrations.AlterField(
            model_name='wage',
            name='transaction_inquiry_response',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wage', to='payment.TransactionInquiryResponse'),
        ),
    ]
