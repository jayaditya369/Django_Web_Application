# Generated by Django 3.1.1 on 2020-12-01 00:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0030_auto_20201130_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 1, 0, 45, 27, 691217, tzinfo=utc)),
        ),
    ]