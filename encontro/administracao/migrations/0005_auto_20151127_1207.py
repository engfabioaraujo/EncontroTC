# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0004_auto_20151127_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='encontro',
            name='alt_usuario_data',
            field=models.DateField(verbose_name='Data de Alteração', default=datetime.datetime(2015, 11, 27, 12, 7, 47, 258347)),
        ),
        migrations.AddField(
            model_name='encontro',
            name='alt_usuario_nome',
            field=models.CharField(max_length=100, default='Administrador'),
        ),
        migrations.AlterField(
            model_name='orgao',
            name='alt_usuario_data',
            field=models.DateField(verbose_name='Data de Alteração', default=datetime.datetime(2015, 11, 27, 12, 7, 47, 255935)),
        ),
    ]
