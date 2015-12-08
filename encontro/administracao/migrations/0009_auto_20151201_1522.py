# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0008_auto_20151201_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encontro',
            name='alt_usuario_data',
            field=models.DateField(verbose_name='Data de Alteração', default=datetime.datetime(2015, 12, 1, 15, 22, 56, 562793)),
        ),
        migrations.AlterField(
            model_name='lider',
            name='alt_usuario_data',
            field=models.DateField(verbose_name='Data de Alteração', default=datetime.datetime(2015, 12, 1, 15, 22, 56, 559311)),
        ),
        migrations.AlterField(
            model_name='lider',
            name='foto',
            field=models.ImageField(upload_to='lideres', default='user-avat.png'),
        ),
        migrations.AlterField(
            model_name='orgao',
            name='alt_usuario_data',
            field=models.DateField(verbose_name='Data de Alteração', default=datetime.datetime(2015, 12, 1, 15, 22, 56, 560459)),
        ),
    ]
