# Generated by Django 3.1.1 on 2020-12-14 18:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0044_auto_20201214_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 14, 18, 17, 40, 735605, tzinfo=utc)),
        ),
    ]