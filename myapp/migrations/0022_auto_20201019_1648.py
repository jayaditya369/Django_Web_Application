# Generated by Django 3.1.1 on 2020-10-19 20:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_auto_20201019_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2020, 10, 19, 20, 48, 33, 139882, tzinfo=utc)),
        ),
    ]
