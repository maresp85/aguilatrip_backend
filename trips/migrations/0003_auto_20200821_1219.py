# Generated by Django 2.2.11 on 2020-08-21 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_city_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='driver_location',
        ),
        migrations.AddField(
            model_name='driver_location',
            name='trip',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='trips.Trip'),
            preserve_default=False,
        ),
    ]
