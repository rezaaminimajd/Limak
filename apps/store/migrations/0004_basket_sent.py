# Generated by Django 3.0.6 on 2020-06-12 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200612_0529'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='sent',
            field=models.BooleanField(default=False),
        ),
    ]
