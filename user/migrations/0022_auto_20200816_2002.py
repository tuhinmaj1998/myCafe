# Generated by Django 3.0.8 on 2020-08-16 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_wallettransaction_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallettransaction',
            name='status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Received', 'Received'), ('Failed', 'Failed'), ('CashBackApplied', 'CashBackApplied')], default='Failed', max_length=100),
        ),
    ]
