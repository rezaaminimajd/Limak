# Generated by Django 3.0.6 on 2020-06-28 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clotheinfo',
            name='clothe',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='information', to='store.Clothe'),
        ),
    ]
