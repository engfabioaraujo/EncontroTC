# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0013_auto_20151201_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgao',
            name='nome',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
