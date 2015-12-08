# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0012_auto_20151201_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encontro',
            name='alt_usuario_data',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data de Alteração'),
        ),
        migrations.AlterField(
            model_name='lider',
            name='alt_usuario_data',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data de Alteração'),
        ),
        migrations.AlterField(
            model_name='orgao',
            name='alt_usuario_data',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data de Alteração'),
        ),
    ]
