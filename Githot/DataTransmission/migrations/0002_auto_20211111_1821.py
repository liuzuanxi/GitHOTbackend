# Generated by Django 3.2.6 on 2021-11-11 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DataTransmission', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='img',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]
