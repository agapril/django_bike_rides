# Generated by Django 4.2.1 on 2023-05-28 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0006_rename_rallies_rally_rename_rides_ride'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ParticipantsList',
        ),
        migrations.DeleteModel(
            name='Rally',
        ),
    ]
