# Generated by Django 4.2.1 on 2023-05-27 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rallies',
            name='description',
            field=models.TextField(default='Lokalny rajd', max_length=50),
        ),
    ]
