# Generated by Django 2.2 on 2020-06-16 12:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0003_auto_20200616_0012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messages',
            old_name='Image',
            new_name='MImage',
        ),
        migrations.AlterField(
            model_name='messages',
            name='sent_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 16, 12, 27, 52, 851854, tzinfo=utc)),
        ),
    ]
