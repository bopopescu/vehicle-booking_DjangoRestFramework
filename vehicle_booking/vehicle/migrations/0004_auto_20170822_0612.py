# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 06:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_auto_20170822_0324'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequisitionTicketLog',
            fields=[
                ('requisitionTicketLogId', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('Bus', 'Bus'), ('MicroBus', 'MicroBus'), ('Car', 'Car')], max_length=8)),
                ('origin', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('ticketStatus', models.CharField(choices=[('Submitted', 'Submitted'), ('Resolved', 'Resolved'), ('Rescheduled', 'Rescheduled')], default='Submitted', max_length=10)),
                ('note', models.CharField(blank=True, max_length=255)),
                ('fromDateTime', models.DateTimeField()),
                ('toDateTime', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('driverId', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle.Driver')),
            ],
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicleNumber',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
