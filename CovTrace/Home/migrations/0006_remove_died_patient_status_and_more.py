# Generated by Django 4.1 on 2022-11-27 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_new_total_number_positive_patients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='died_patient',
            name='status',
        ),
        migrations.RemoveField(
            model_name='new_total_number_positive_patients',
            name='status',
        ),
        migrations.RemoveField(
            model_name='recovered_patient',
            name='status',
        ),
    ]