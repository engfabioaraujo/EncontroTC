# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cancelamento',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('valor_devolvido', models.FloatField(default=0.0)),
                ('data_cancelamento', models.DateField(verbose_name='Data de Cancelamento')),
                ('motivo', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Encontro',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('tema', models.CharField(max_length=200)),
                ('ano', models.IntegerField(default=2015)),
                ('vagas', models.IntegerField(default=200)),
                ('ativo', models.BooleanField(default=True)),
                ('valor', models.FloatField(default=150.0)),
            ],
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('data_inscricao', models.DateField(verbose_name='Data de Inscrição')),
                ('cancelado', models.BooleanField(default=False)),
                ('cancelamento', models.ForeignKey(to='administracao.Cancelamento', verbose_name='Cancelamento')),
            ],
        ),
        migrations.CreateModel(
            name='Lider',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('sobrenomenome', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=100)),
                ('sexo', models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')], verbose_name='Sexo')),
                ('data_nascimento', models.DateField(verbose_name='Data de nascimento')),
                ('foto', models.FileField(upload_to='lideres')),
                ('cargo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Observacao',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(max_length=500)),
                ('lider', models.ForeignKey(to='administracao.Lider', verbose_name='Lider')),
            ],
        ),
        migrations.CreateModel(
            name='Orgao',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('sobrenomenome', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=100)),
                ('sexo', models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')], verbose_name='Sexo')),
                ('camisa', models.CharField(max_length=2, choices=[('GG', 'Extra Grande - GG'), ('G', 'Grande - G'), ('M', 'Médio - M'), ('P', 'Pequeno - P'), ('PP', 'Pequeno - PP')], verbose_name='Sexo')),
                ('organizacao', models.BooleanField(default=True)),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('foto', models.FileField(upload_to='participantes')),
                ('observacoes', models.ManyToManyField(to='administracao.Observacao')),
                ('orgao', models.ForeignKey(to='administracao.Orgao', verbose_name='Orgao')),
            ],
        ),
        migrations.CreateModel(
            name='Quarto',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('responsavel', models.ForeignKey(to='administracao.Lider', verbose_name='Lider')),
            ],
        ),
        migrations.AddField(
            model_name='participante',
            name='quarto',
            field=models.ForeignKey(to='administracao.Quarto', verbose_name='Quarto'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='participante',
            field=models.ForeignKey(to='administracao.Participante', verbose_name='Participante'),
        ),
        migrations.AddField(
            model_name='equipe',
            name='membros',
            field=models.ManyToManyField(to='administracao.Lider'),
        ),
        migrations.AddField(
            model_name='encontro',
            name='inscricoes',
            field=models.ManyToManyField(to='administracao.Inscricao'),
        ),
    ]
