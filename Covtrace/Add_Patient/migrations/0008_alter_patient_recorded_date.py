# Generated by Django 4.1 on 2022-11-25 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Add_Patient', '0007_patient_recorded_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='recorded_date',
            field=models.DateField(blank=True),
        ),
    ]
