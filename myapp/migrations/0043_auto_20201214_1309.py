# Generated by Django 3.1.1 on 2020-12-14 18:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0042_auto_20201212_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 14, 18, 9, 47, 392741, tzinfo=utc)),
        ),
    ]
