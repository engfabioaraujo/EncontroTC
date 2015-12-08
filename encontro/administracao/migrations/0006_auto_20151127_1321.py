# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0005_auto_20151127_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='lider',
            name='alt_usuario_data',
            field=models.DateField(default=datetime.datetime(2015, 11, 27, 13, 21, 41, 39029), verbose_name='Data de Alteração'),
        ),
        migrations.AddField(
            model_name='lider',
            name='alt_usuario_nome',
            field=models.CharField(default='Administrador', max_length=100),
        ),
        migrations.AlterField(
            model_name='encontro',
            name='alt_usuario_data',
            field=models.DateField(default=datetime.datetime(2015, 11, 27, 13, 21, 41, 42435), verbose_name='Data de Alteração'),
        ),
        migrations.AlterField(
            model_name='orgao',
            name='alt_usuario_data',
            field=models.DateField(default=datetime.datetime(2015, 11, 27, 13, 21, 41, 40074), verbose_name='Data de Alteração'),
        ),
    ]
