# Generated by Django 3.2.6 on 2021-10-11 15:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermartapp', '0012_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='time',
            field=models.TimeField(default=datetime.time(21, 25, 24, 321010)),
        ),
    ]
