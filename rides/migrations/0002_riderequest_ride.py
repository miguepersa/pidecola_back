# Generated by Django 5.0.2 on 2024-03-04 23:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='riderequest',
            name='ride',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rides.ride'),
        ),
    ]
