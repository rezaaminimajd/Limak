# Generated by Django 3.0.6 on 2020-06-12 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionCreatorRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionInquiryResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('track_id', models.IntegerField()),
                ('id_pay_id', models.CharField(max_length=512)),
                ('order_id', models.CharField(max_length=512)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Wage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('by', models.CharField(max_length=32)),
                ('type', models.CharField(max_length=32)),
                ('amount', models.IntegerField()),
                ('transaction_inquiry_response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wage', to='payment.TransactionInquiryResponse')),
            ],
        ),
        migrations.CreateModel(
            name='Verify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField()),
                ('transaction_inquiry_response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verify', to='payment.TransactionInquiryResponse')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pay_id', models.CharField(max_length=512, unique=True)),
                ('link', models.CharField(max_length=512)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('phone', models.CharField(blank=True, max_length=64, null=True)),
                ('mail', models.CharField(blank=True, max_length=64, null=True)),
                ('desc', models.CharField(blank=True, max_length=256, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactions', to='store.Basket')),
            ],
        ),
        migrations.CreateModel(
            name='Settlement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_id', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('date', models.IntegerField()),
                ('transaction_inquiry_response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='settlement', to='payment.TransactionInquiryResponse')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_id', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('card_no', models.CharField(max_length=1024)),
                ('hashed_card_no', models.CharField(max_length=1024)),
                ('date', models.IntegerField()),
                ('transaction_inquiry_response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='payment.TransactionInquiryResponse')),
            ],
        ),
        migrations.CreateModel(
            name='Payer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
                ('mail', models.CharField(max_length=128)),
                ('desc', models.CharField(max_length=1024)),
                ('transaction_inquiry_response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payer', to='payment.TransactionInquiryResponse')),
            ],
        ),
    ]
