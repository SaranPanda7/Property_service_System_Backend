# Generated by Django 3.2.12 on 2022-05-06 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PropertyServiceApp', '0018_propertymonitoring'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestmentAdvice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_id', models.CharField(blank=True, max_length=255, null=True)),
                ('property_size', models.CharField(blank=True, max_length=55, null=True)),
                ('land_size', models.CharField(blank=True, max_length=255, null=True)),
                ('beds', models.CharField(blank=True, max_length=255, null=True)),
                ('baths', models.CharField(blank=True, max_length=255, null=True)),
                ('garage', models.CharField(blank=True, max_length=255, null=True)),
                ('garage_size', models.CharField(blank=True, max_length=255, null=True)),
                ('build_year', models.CharField(blank=True, max_length=255, null=True)),
                ('property_features', models.JSONField(blank=True, null=True)),
                ('available_days', models.JSONField(blank=True, null=True)),
                ('available_time', models.JSONField(blank=True, null=True)),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='investment_advice', to='PropertyServiceApp.users')),
            ],
        ),
    ]