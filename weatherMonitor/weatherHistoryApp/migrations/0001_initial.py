# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=50)),
                ('url_suffix', models.CharField(default=b'', max_length=30)),
                ('created_at', models.DateTimeField(default=b'2016-06-27 10:48:22')),
            ],
        ),
    ]
