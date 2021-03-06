# Generated by Django 2.2.11 on 2020-08-21 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0008_auto_20200821_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='start_trip',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='trips.City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='start_trip',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='trips.Country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stop_trip',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='trips.City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stop_trip',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='trips.Country'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='start_trip',
            name='pickup_address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stop_trip',
            name='pickup_address',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
