# Generated by Django 3.1.1 on 2020-10-19 20:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20201019_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2020, 10, 19, 20, 31, 40, 858123, tzinfo=utc)),
        ),
    ]
