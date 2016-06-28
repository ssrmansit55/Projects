# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('weatherHistoryApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='created_at',
            field=models.DateTimeField(default=b'2016-06-27 11:15:03'),
        ),
        migrations.AlterField(
            model_name='station',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True, validators=[django.core.validators.MaxValueValidator(99999999), django.core.validators.MinValueValidator(10000000)]),
        ),
    ]
