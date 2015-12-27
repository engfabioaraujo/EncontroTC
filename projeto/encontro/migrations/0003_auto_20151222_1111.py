# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encontro', '0002_auto_20151222_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipe',
            name='encontro',
            field=models.ForeignKey(to='encontro.Encontro'),
        ),
        migrations.AlterField(
            model_name='lider',
            name='encontro',
            field=models.ForeignKey(to='encontro.Encontro'),
        ),
        migrations.AlterField(
            model_name='quarto',
            name='encontro',
            field=models.ForeignKey(to='encontro.Encontro'),
        ),
    ]
