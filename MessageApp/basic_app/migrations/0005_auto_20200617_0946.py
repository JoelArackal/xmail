# Generated by Django 2.2 on 2020-06-17 04:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0004_auto_20200616_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='MFile',
            field=models.FileField(blank=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='sent_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 17, 4, 16, 21, 67860, tzinfo=utc)),
        ),
    ]
