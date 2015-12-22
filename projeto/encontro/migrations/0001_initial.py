# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cancelamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('valor_devolvido', models.FloatField(default=0.0)),
                ('data_cancelamento', models.DateField(verbose_name='Data de Cancelamento')),
                ('motivo', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Encontro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('ano', models.IntegerField(default=2015, unique=True)),
                ('tema', models.CharField(max_length=200)),
                ('vagas', models.IntegerField(default=200)),
                ('ativo', models.BooleanField(default=True)),
                ('valor', models.FloatField(default=150.0)),
                ('alt_usuario_nome', models.CharField(default='Administrador', max_length=100)),
                ('alt_usuario_data', models.DateField(default=django.utils.timezone.now, verbose_name='Data de Alteração')),
            ],
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('data_inscricao', models.DateField(verbose_name='Data de Inscrição')),
                ('cancelado', models.BooleanField(default=False)),
                ('cancelamento', models.ForeignKey(verbose_name='Cancelamento', to='encontro.Cancelamento')),
                ('encontro', models.ForeignKey(default=None, to='encontro.Encontro', verbose_name='Encontro')),
            ],
        ),
        migrations.CreateModel(
            name='Lider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=100)),
                ('sexo', models.CharField(max_length=1, verbose_name='Sexo', choices=[('M', 'Masculino'), ('F', 'Feminino')])),
                ('data_nascimento', models.DateField(default=django.utils.timezone.now, verbose_name='Data de nascimento')),
                ('foto', models.ImageField(default='user-avat.png', upload_to='lideres')),
                ('cargo', models.CharField(max_length=12, verbose_name='Posição na Igreja', choices=[('Membro', 'Membro'), ('Auxíliar', 'Auxíliar'), ('Diácono', 'Diácono'), ('Presbítero', 'Presbítero'), ('Evangelísta', 'Evangelísta'), ('Pastor', 'Pastor')])),
                ('alt_usuario_nome', models.CharField(default='Administrador', max_length=100)),
                ('alt_usuario_data', models.DateField(default=django.utils.timezone.now, verbose_name='Data de Alteração')),
            ],
        ),
        migrations.CreateModel(
            name='Observacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('descricao', models.TextField(max_length=500)),
                ('lider', models.ForeignKey(verbose_name='Lider', to='encontro.Lider')),
            ],
        ),
        migrations.CreateModel(
            name='Orgao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('alt_usuario_nome', models.CharField(default='Administrador', max_length=100)),
                ('alt_usuario_data', models.DateField(default=django.utils.timezone.now, verbose_name='Data de Alteração')),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=20)),
                ('sobrenomenome', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=100)),
                ('sexo', models.CharField(max_length=1, verbose_name='Sexo', choices=[('M', 'Masculino'), ('F', 'Feminino')])),
                ('camisa', models.CharField(max_length=2, verbose_name='Sexo', choices=[('GG', 'Extra Grande - GG'), ('G', 'Grande - G'), ('M', 'Médio - M'), ('P', 'Pequeno - P'), ('PP', 'Pequeno - PP')])),
                ('organizacao', models.BooleanField(default=True)),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('foto', models.FileField(upload_to='participantes')),
                ('observacoes', models.ManyToManyField(to='encontro.Observacao')),
                ('orgao', models.ForeignKey(verbose_name='Orgao', to='encontro.Orgao')),
            ],
        ),
        migrations.CreateModel(
            name='Quarto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('alt_usuario_nome', models.CharField(default='Administrador', max_length=100)),
                ('alt_usuario_data', models.DateField(default=django.utils.timezone.now, verbose_name='Data de Alteração')),
                ('encontro', models.ForeignKey(verbose_name='Encontro', to='encontro.Encontro')),
                ('responsaveis', models.ManyToManyField(verbose_name='Líderes Responsáveis', to='encontro.Lider')),
            ],
        ),
        migrations.AddField(
            model_name='participante',
            name='quarto',
            field=models.ForeignKey(verbose_name='Quarto', to='encontro.Quarto'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='participante',
            field=models.ForeignKey(verbose_name='Participante', to='encontro.Participante'),
        ),
        migrations.AddField(
            model_name='equipe',
            name='membros',
            field=models.ManyToManyField(to='encontro.Lider'),
        ),
    ]
