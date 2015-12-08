# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0006_auto_20151127_1321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lider',
            old_name='sobrenomenome',
            new_name='sobrenome',
        ),
        migrations.AlterField(
            model_name='encontro',
            name='alt_usuario_data',
            field=models.DateField(default=datetime.datetime(2015, 11, 27, 14, 5, 35, 378167), verbose_name='Data de Alteração'),
        ),
        migrations.AlterField(
            model_name='lider',
            name='alt_usuario_data',
            field=models.DateField(default=datetime.datetime(2015, 11, 27, 14, 5, 35, 374743), verbose_name='Data de Alteração'),
        ),
        migrations.AlterField(
            model_name='lider',
            name='cargo',
            field=models.CharField(choices=[('Membro', 'Membro'), ('Auxíliar', 'Auxíliar'), ('Diácono', 'Diácono'), ('Presbítero', 'Presbítero'), ('Evangelísta', 'Evangelísta')], max_length=12, verbose_name='Posição na Igreja'),
        ),
        migrations.AlterField(
            model_name='orgao',
            name='alt_usuario_data',
            field=models.DateField(default=datetime.datetime(2015, 11, 27, 14, 5, 35, 375783), verbose_name='Data de Alteração'),
        ),
    ]
