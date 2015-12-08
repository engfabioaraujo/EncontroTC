# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0010_auto_20151201_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='lider',
            name='data_nascimento',
            field=models.DateField(default=datetime.date(2015, 12, 1), verbose_name='Data de nascimento'),
        ),
        migrations.AlterField(
            model_name='encontro',
            name='alt_usuario_data',
            field=models.DateField(default=datetime.date(2015, 12, 1), verbose_name='Data de Alteração'),
        ),
        migrations.AlterField(
            model_name='lider',
            name='alt_usuario_data',
            field=models.DateField(default=datetime.date(2015, 12, 1), verbose_name='Data de Alteração'),
        ),
        migrations.AlterField(
            model_name='orgao',
            name='alt_usuario_data',
            field=models.DateField(default=datetime.date(2015, 12, 1), verbose_name='Data de Alteração'),
        ),
    ]
