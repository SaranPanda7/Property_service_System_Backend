# Generated by Django 3.2.12 on 2022-05-02 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PropertyServiceApp', '0007_propertytracing_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertytracing',
            name='available_days',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='propertytracing',
            name='available_time',
            field=models.TextField(),
        ),
    ]