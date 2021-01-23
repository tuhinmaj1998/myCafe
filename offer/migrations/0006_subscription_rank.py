# Generated by Django 3.0.8 on 2020-08-08 11:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0005_subscription_color_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='rank',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
    ]