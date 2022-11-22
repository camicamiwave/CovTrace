# Generated by Django 4.1 on 2022-11-07 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covtrace_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birthday', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('barangay', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]