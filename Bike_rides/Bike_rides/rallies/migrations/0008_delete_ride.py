# Generated by Django 4.2.1 on 2023-06-11 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rallies', '0007_alter_ride_start_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ride',
        ),
    ]