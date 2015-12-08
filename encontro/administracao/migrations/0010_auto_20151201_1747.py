# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0009_auto_20151201_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lider',
            name='data_nascimento',
        ),
        migrations.AlterField(
            model_name='encontro',
            name='alt_usuario_data',
            field=models.DateField(verbose_name='Data de Alteração', default=datetime.datetime(2015, 12, 1, 17, 47, 47, 199152)),
        ),
        migrations.AlterField(
            model_name='lider',
            name='alt_usuario_data',
            field=models.DateField(verbose_name='Data de Alteração', default=datetime.datetime(2015, 12, 1, 17, 47, 47, 195675)),
        ),
        migrations.AlterField(
            model_name='orgao',
            name='alt_usuario_data',
            field=models.DateField(verbose_name='Data de Alteração', default=datetime.datetime(2015, 12, 1, 17, 47, 47, 196806)),
        ),
    ]
