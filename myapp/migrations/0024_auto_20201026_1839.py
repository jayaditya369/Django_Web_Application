# Generated by Django 3.1.1 on 2020-10-26 22:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_auto_20201021_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2020, 10, 26, 22, 39, 0, 742936, tzinfo=utc)),
        ),
    ]
