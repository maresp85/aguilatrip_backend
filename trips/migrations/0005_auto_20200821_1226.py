# Generated by Django 2.2.11 on 2020-08-21 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0004_auto_20200821_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='driver_location',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='start_trip',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='stop_trip',
        ),
        migrations.AddField(
            model_name='driver_location',
            name='trip',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='trips.Trip'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='start_trip',
            name='trip',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='trips.Trip'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stop_trip',
            name='trip',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='trips.Trip'),
            preserve_default=False,
        ),
    ]