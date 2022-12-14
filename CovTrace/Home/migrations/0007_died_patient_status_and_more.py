# Generated by Django 4.1 on 2022-11-27 02:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_remove_died_patient_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='died_patient',
            name='status',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='new_total_number_positive_patients',
            name='status',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recovered_patient',
            name='status',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]