# Generated by Django 3.2.12 on 2022-05-05 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PropertyServiceApp', '0011_auto_20220505_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertytracing',
            name='available_days',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='propertytracing',
            name='available_time',
            field=models.JSONField(),
        ),
    ]