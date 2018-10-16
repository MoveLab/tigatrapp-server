# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-18 11:56
from __future__ import unicode_literals
from south.v2 import SchemaMigration

'''
    These migrations are incompatible with South, and break all other migrations. Therefore, they are commented and there
    only are skeleton empty migrations 
'''

'''
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tigapublic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Epidemiology',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('address', models.CharField(blank=True, max_length=225, null=True)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('health_centre', models.CharField(blank=True, max_length=225, null=True)),
                ('age', models.IntegerField()),
                ('country', models.CharField(blank=True, max_length=225, null=True)),
                ('date_arribal', models.DateTimeField(blank=True, null=True)),
                ('date_symptom', models.DateTimeField(blank=True, null=True)),
                ('patient_state', models.CharField(blank=True, max_length=225, null=True)),
                ('comments', models.TextField(blank=True, default=None, help_text='Extra comments for patients', null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='municipalities',
            name='codprov',
            field=models.ForeignKey(db_column='codprov', on_delete=django.db.models.deletion.CASCADE, to='tigapublic.Province'),
        ),
    ]
'''

class Migration(SchemaMigration):

    def forwards(self, orm):
        pass

    def backwards(self, orm):
        pass

    complete_apps = ['tigapublic']