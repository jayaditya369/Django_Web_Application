# Generated by Django 3.1.1 on 2020-10-19 19:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20201019_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2020, 10, 19, 19, 58, 46, 966938, tzinfo=utc)),
        ),
    ]
