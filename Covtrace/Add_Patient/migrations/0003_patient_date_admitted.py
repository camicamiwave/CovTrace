# Generated by Django 4.1 on 2022-11-20 01:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Add_Patient', '0002_patient_latitude_patient_longitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='date_admitted',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 11, 20, 1, 29, 21, 645060, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]