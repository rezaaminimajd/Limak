# Generated by Django 3.0.6 on 2020-06-24 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_basket_sent'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='clotheinfo',
            constraint=models.UniqueConstraint(fields=('clothe', 'color', 'size'), name='unique_clothe_info'),
        ),
    ]
