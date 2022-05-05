# Generated by Django 3.2.12 on 2022-05-05 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PropertyServiceApp', '0010_alter_propertytracing_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertytracing',
            name='user_id',
        ),
        migrations.AddField(
            model_name='propertytracing',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='property_tracing', to='PropertyServiceApp.users'),
        ),
    ]