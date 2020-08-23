# Generated by Django 2.2.11 on 2020-08-21 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='trips.Country'),
            preserve_default=False,
        ),
    ]