# Generated by Django 3.1.1 on 2020-10-19 20:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_auto_20201019_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2020, 10, 19, 20, 45, 32, 436108, tzinfo=utc)),
        ),
    ]
