# Generated by Django 3.2.12 on 2022-03-21 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PropertyServiceApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='PropertyServiceApp.roles'),
        ),
    ]
