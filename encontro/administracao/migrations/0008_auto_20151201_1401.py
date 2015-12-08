# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0007_auto_20151127_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encontro',
            name='alt_usuario_data',
            field=models.DateField(verbose_name='Data de Alteração', default=datetime.datetime(2015, 12, 1, 14, 1, 49, 785657)),
        ),
        migrations.AlterField(
            model_name='lider',
            name='alt_usuario_data',
            field=models.DateField(verbose_name='Data de Alteração', default=datetime.datetime(2015, 12, 1, 14, 1, 49, 782224)),
        ),
        migrations.AlterField(
            model_name='orgao',
            name='alt_usuario_data',
            field=models.DateField(verbose_name='Data de Alteração', default=datetime.datetime(2015, 12, 1, 14, 1, 49, 783292)),
        ),
    ]
