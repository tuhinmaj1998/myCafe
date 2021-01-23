# Generated by Django 3.0.8 on 2020-08-15 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_auto_20200815_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='useWallet',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='order',
            name='walletDeduction',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
