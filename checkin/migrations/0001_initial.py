# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location_name', models.CharField(max_length=50)),
                ('location_type', models.CharField(max_length=2, choices=[(b'fb', b'Food Bank'), (b'cb', b'Club Bamboo')])),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('barcode_id', models.CharField(max_length=7, serialize=False, primary_key=b'True')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='attendancerecord',
            name='location',
            field=models.ForeignKey(to='checkin.Location', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='attendancerecord',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='checkin.Member', null=True),
        ),
    ]
