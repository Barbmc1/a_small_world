# Generated by Django 2.2.1 on 2019-06-06 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_small_world', '0006_auto_20190606_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturers',
            name='manufacturer_address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='manufacturers',
            name='manufacturer_city',
            field=models.CharField(max_length=25),
        ),
    ]
