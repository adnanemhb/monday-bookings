# Generated by Django 4.2.5 on 2023-09-22 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_alter_booking_booking_value_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='creation_log',
            field=models.DateTimeField(null=True),
        ),
    ]
