# Generated by Django 3.0.5 on 2020-04-15 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule3', '0008_timetable_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='room_number',
            field=models.IntegerField(default=0),
        ),
    ]
