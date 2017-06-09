# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 23:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0008_auto_20170606_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_id', models.PositiveIntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('visit_type', models.CharField(default='list', max_length=50)),
                ('record_id', models.PositiveIntegerField(default=0)),
                ('patient_id', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]