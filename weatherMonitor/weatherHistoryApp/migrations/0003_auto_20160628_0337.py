# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weatherHistoryApp', '0002_auto_20160627_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='created_at',
            field=models.DateTimeField(default=b'2016-06-28 03:37:38'),
        ),
        migrations.AlterField(
            model_name='station',
            name='url_suffix',
            field=models.CharField(default=b'', max_length=70),
        ),
    ]
