# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='stock',
            field=models.CharField(default='aapl', max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='stockPrice',
            field=models.DecimalField(default=100.0, max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
    ]
