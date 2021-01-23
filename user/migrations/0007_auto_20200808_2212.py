# Generated by Django 3.0.8 on 2020-08-08 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200808_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='adminnote',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Expired', 'Expired'), ('Cancelled', 'Cancelled')], default='Cancelled', max_length=10),
        ),
    ]
