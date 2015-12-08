# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0011_auto_20151201_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lider',
            name='data_nascimento',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data de nascimento'),
        ),
    ]
