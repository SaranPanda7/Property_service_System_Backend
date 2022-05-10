# Generated by Django 3.2.12 on 2022-05-08 13:41

import PropertyServiceApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PropertyServiceApp', '0003_auto_20220508_0205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investmentadvice',
            name='id',
        ),
        migrations.RemoveField(
            model_name='legalissues',
            name='id',
        ),
        migrations.RemoveField(
            model_name='otherservices',
            name='id',
        ),
        migrations.RemoveField(
            model_name='propertymonitoring',
            name='id',
        ),
        migrations.AddField(
            model_name='investmentadvice',
            name='service_id',
            field=models.CharField(default=PropertyServiceApp.models.create_investmentAdvice_servId, max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='investmentadvice',
            name='sno',
            field=models.IntegerField(default=PropertyServiceApp.models.ia_records_count),
        ),
        migrations.AddField(
            model_name='legalissues',
            name='service_id',
            field=models.CharField(default=PropertyServiceApp.models.create_legalIssues_servId, max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='legalissues',
            name='sno',
            field=models.IntegerField(default=PropertyServiceApp.models.li_records_count),
        ),
        migrations.AddField(
            model_name='otherservices',
            name='service_id',
            field=models.CharField(default=PropertyServiceApp.models.create_otherServices_servId, max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='otherservices',
            name='sno',
            field=models.IntegerField(default=PropertyServiceApp.models.os_records_count),
        ),
        migrations.AddField(
            model_name='propertymonitoring',
            name='service_id',
            field=models.CharField(default=PropertyServiceApp.models.create_propertyMonitoring_servId, max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='propertymonitoring',
            name='sno',
            field=models.IntegerField(default=PropertyServiceApp.models.pm_records_count),
        ),
    ]