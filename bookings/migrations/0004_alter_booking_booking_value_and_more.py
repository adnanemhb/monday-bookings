# Generated by Django 4.2.5 on 2023-09-22 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_booking_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_in_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='creation_log',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='flat_booked',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='guest_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]