# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('encontro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancelamento',
            name='alt_usuario_data',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data de Alteração'),
        ),
        migrations.AddField(
            model_name='cancelamento',
            name='alt_usuario_nome',
            field=models.CharField(default='Administrador', max_length=100),
        ),
        migrations.AddField(
            model_name='equipe',
            name='alt_usuario_data',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data de Alteração'),
        ),
        migrations.AddField(
            model_name='equipe',
            name='alt_usuario_nome',
            field=models.CharField(default='Administrador', max_length=100),
        ),
        migrations.AddField(
            model_name='equipe',
            name='encontro',
            field=models.ForeignKey(to='encontro.Encontro', default=1),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='alt_usuario_data',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data de Alteração'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='alt_usuario_nome',
            field=models.CharField(default='Administrador', max_length=100),
        ),
        migrations.AddField(
            model_name='lider',
            name='encontro',
            field=models.ForeignKey(to='encontro.Encontro', default=1),
        ),
        migrations.AddField(
            model_name='observacao',
            name='alt_usuario_data',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data de Alteração'),
        ),
        migrations.AddField(
            model_name='observacao',
            name='alt_usuario_nome',
            field=models.CharField(default='Administrador', max_length=100),
        ),
        migrations.AddField(
            model_name='participante',
            name='alt_usuario_data',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data de Alteração'),
        ),
        migrations.AddField(
            model_name='participante',
            name='alt_usuario_nome',
            field=models.CharField(default='Administrador', max_length=100),
        ),
        migrations.AlterField(
            model_name='quarto',
            name='encontro',
            field=models.ForeignKey(to='encontro.Encontro', default=1),
        ),
    ]
