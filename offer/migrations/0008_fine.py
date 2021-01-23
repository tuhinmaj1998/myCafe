# Generated by Django 3.0.8 on 2020-08-09 04:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0007_auto_20200808_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('description', models.CharField(blank=True, max_length=150)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('percentage', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
    ]
