# Generated by Django 2.2 on 2020-06-15 12:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='sent_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 15, 12, 31, 33, 855133, tzinfo=utc)),
        ),
    ]
