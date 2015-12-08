# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0003_auto_20151115_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgao',
            name='alt_usuario_data',
            field=models.DateField(verbose_name='Data de Alteração', default=datetime.datetime(2015, 11, 27, 11, 58, 50, 718214)),
        ),
        migrations.AddField(
            model_name='orgao',
            name='alt_usuario_nome',
            field=models.CharField(max_length=100, default='Administrador'),
        ),
    ]
