# Generated by Django 3.0.8 on 2020-08-11 15:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0021_auto_20200811_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdiscount',
            name='expiryDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]