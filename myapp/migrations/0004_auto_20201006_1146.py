# Generated by Django 3.1.1 on 2020-10-06 15:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20201006_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(verbose_name=django.utils.timezone.now),
        ),
    ]
