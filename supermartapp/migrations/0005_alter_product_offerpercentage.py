# Generated by Django 3.2.6 on 2021-09-24 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermartapp', '0004_auto_20210925_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='offerPercentage',
            field=models.TextField(),
        ),
    ]
