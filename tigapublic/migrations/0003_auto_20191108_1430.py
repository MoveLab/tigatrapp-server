# Generated by Django 2.2.7 on 2019-11-08 14:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tigapublic', '0002_auto_20191108_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stormdrain',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 8, 14, 29, 50, 563190), null=True),
        ),
        migrations.AlterField(
            model_name='stormdrainuserversions',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 8, 14, 29, 50, 565746)),
        ),
    ]
