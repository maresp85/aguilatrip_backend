# Generated by Django 2.2.11 on 2020-08-24 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0017_auto_20200824_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(max_length=30, null=True),
        ),
    ]