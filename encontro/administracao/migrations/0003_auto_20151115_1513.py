# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0002_auto_20151113_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encontro',
            name='inscricoes',
        ),
        migrations.AddField(
            model_name='inscricao',
            name='encontro',
            field=models.ForeignKey(verbose_name='Encontro', default=None, to='administracao.Encontro'),
        ),
        migrations.AlterField(
            model_name='encontro',
            name='ano',
            field=models.IntegerField(default=2015, unique=True),
        ),
    ]
