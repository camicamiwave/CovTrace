# Generated by Django 4.1 on 2022-11-17 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Add_Patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='patient',
            name='longitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='patient',
            name='population',
            field=models.FloatField(default=1),
        ),
    ]
