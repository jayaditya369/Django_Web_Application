# Generated by Django 3.1.1 on 2020-12-01 15:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0032_auto_20201201_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 1, 15, 32, 2, 523876, tzinfo=utc)),
        ),
    ]