# Generated by Django 4.2.5 on 2023-09-22 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_apicallrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='item_id',
            field=models.BigIntegerField(null=True),
        ),
    ]
