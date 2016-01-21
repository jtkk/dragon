# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0002_member_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('barcode_id', models.CharField(max_length=7, serialize=False, primary_key=b'True')),
                ('client_id', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address1', models.CharField(max_length=50, null=b'True')),
                ('address2', models.CharField(max_length=50, null=b'True')),
                ('city', models.CharField(max_length=25, null=b'True')),
                ('state', models.CharField(max_length=25, null=b'True')),
                ('zipcode', models.CharField(max_length=5, null=b'True')),
            ],
        ),
        migrations.RenameField(
            model_name='attendancerecord',
            old_name='location',
            new_name='location_id',
        ),
        migrations.RemoveField(
            model_name='attendancerecord',
            name='member',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.AddField(
            model_name='attendancerecord',
            name='client_barcode_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='checkin.Client', null=True),
        ),
    ]
