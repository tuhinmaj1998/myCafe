# Generated by Django 3.0.8 on 2020-08-23 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0029_useraddress_locationaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
