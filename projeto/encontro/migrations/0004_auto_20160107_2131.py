# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encontro', '0003_auto_20151222_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encontro',
            name='ano',
            field=models.IntegerField(default=2016, unique=True),
        ),
    ]
