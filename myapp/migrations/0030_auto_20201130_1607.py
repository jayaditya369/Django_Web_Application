# Generated by Django 3.1.1 on 2020-11-30 21:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_auto_20201124_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2020, 11, 30, 21, 7, 9, 609444, tzinfo=utc)),
        ),
    ]
