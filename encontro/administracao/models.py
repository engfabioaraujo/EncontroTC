# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from datetime  import date

import datetime

# Classe Lider
class Lider(models.Model):

    #Tipos de Sexo
    CHOICES_SEXO = (('M', 'Masculino'), ('F', 'Feminino'))
    #Tipo de Cargo
    CHOICES_CARGO = (('Membro', 'Membro'),
                     ('Auxíliar', 'Auxíliar'),
                     ('Diácono' , 'Diácono'),
                     ('Presbítero', 'Presbítero'),
                     ('Evangelísta', 'Evangelísta'),
                     ('Pastor', 'Pastor'))

    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=13)
    email = models.EmailField(max_length=100)
    sexo = models.CharField(u'Sexo', max_length=1, choices=CHOICES_SEXO)
    data_nascimento = models.DateField(u'Data de nascimento', default=timezone.now)
    foto = models.ImageField(upload_to="lideres", default='user-avat.png')

    cargo = models.CharField(u'Posição na Igreja', max_length=12, choices=CHOICES_CARGO)

    alt_usuario_nome = models.CharField(max_length=100, default="Administrador")
    alt_usuario_data = models.DateField(u'Data de Alteração', default=timezone.now)

    def get_sigla_cargo(self):
        if self.cargo == 'Auxíliar':
            return 'Aux.'
        elif self.cargo == 'Diácono':
            return 'Dc.'
        elif self.cargo == 'Presbítero':
            return 'Pb.'
        elif self.cargo == 'Evangelísta':
            return 'Ev.'
        elif self.cargo == 'Pastor':
            return 'Pr.'
        else:
            return ''

    def __str__(self):
        sigla = self.get_sigla_cargo()
        return '%s %s %s - %s' % (sigla, self.nome, self.sobrenome, self.telefone)

    def get_nome_completo(self):
        sigla = self.get_sigla_cargo()
        return '%s %s %s' % (sigla, self.nome, self.sobrenome)

    def get_ultima_alteracao(self):
        return '%s - %s' % (self.alt_usuario_nome, self.alt_usuario_data)

# Classe Quarto
class Quarto(models.Model):

    nome = models.CharField(max_length=30)
    responsaveis = models.ManyToManyField(Lider, verbose_name=u'Líderes Responsáveis')
    encontro = models.ForeignKey(Encontro, verbose_name=u'Encontro')

    alt_usuario_nome = models.CharField(max_length=100, default="Administrador")
    alt_usuario_data = models.DateField(u'Data de Alteração', default=timezone.now)

    def __str__(self):
        return self.nome

    def get_ultima_alteracao(self):
        return '%s - %s' % (self.alt_usuario_nome, self.alt_usuario_data)

    def get_responsaveis(self):
        return 'IMPLEMENTAR'

# Classe Orgão
class Orgao(models.Model):

    nome = models.CharField(max_length=50, unique=True)

    alt_usuario_nome = models.CharField(max_length=100, default="Administrador")
    alt_usuario_data = models.DateField(u'Data de Alteração', default=timezone.now)

    def __str__(self):
        return self.nome

    def get_ultima_alteracao(self):
        return '%s - %s' % (self.alt_usuario_nome, self.alt_usuario_data)

# Classe Observação
class Observacao(models.Model):

    descricao = models.TextField(max_length=500)
    lider = models.ForeignKey(Lider, verbose_name=u'Lider')

    def __str__(self):
        return self.descricao

# Classe Participante
class Participante(models.Model):

    #Tipos de Sexo
    ESCOLHA_SEXO = (('M', 'Masculino'), ('F', 'Feminino'))

    #Tipos de Camisa
    ESCOLHA_CAMISA = (('GG', 'Extra Grande - GG'), ('G', 'Grande - G'), ('M', 'Médio - M'), ('P', 'Pequeno - P'), ('PP', 'Pequeno - PP'))

    nome = models.CharField(max_length=20)
    sobrenomenome = models.CharField(max_length=20)
    telefone = models.CharField(max_length=13)
    email = models.EmailField(max_length=100)
    sexo = models.CharField(u'Sexo', max_length=1, choices=ESCOLHA_SEXO)
    camisa = models.CharField(u'Sexo', max_length=2, choices=ESCOLHA_CAMISA)
    organizacao = models.BooleanField(default=True)
    data_nascimento = models.DateField(u'Data de Nascimento')
    foto = models.FileField(upload_to="participantes")

     #relacionamentos
    quarto = models.ForeignKey(Quarto, verbose_name=u'Quarto')
    orgao = models.ForeignKey(Orgao, verbose_name=u'Orgao')
    observacoes = models.ManyToManyField(Observacao)

    def __str__(self):
        return '%s %s - %s' % (self.nome, self.sobrenomenome, self.telefone)

    def nome_completo(self):
        return '%s %s' % (self.nome, self.sobrenomenome)

# Classe Encontro de Jovens
class Encontro(models.Model):

    ano = models.IntegerField(default=date.today().year, unique=True)
    tema = models.CharField(max_length=200)
    vagas = models.IntegerField(default=200)
    ativo = models.BooleanField(default=True)
    valor = models.FloatField(default=150.00)

    alt_usuario_nome = models.CharField(max_length=100, default="Administrador")
    alt_usuario_data = models.DateField(u'Data de Alteração', default=timezone.now)

    #relacionamentos
    #inscricoes = models.ManyToManyField(Inscricao)

    #def vagas_disponiveis(self):
    #    return vagas - len(inscricoes)

    def __str__(self):
        return '%s - %s' % (self.ano, self.tema)

    def get_ultima_alteracao(self):
        return '%s - %s' % (self.alt_usuario_nome, self.alt_usuario_data)

# Classe Cancelamento de Inscrição
class Cancelamento(models.Model):

    valor_devolvido = models.FloatField(default=0.00)
    data_cancelamento = models.DateField(u'Data de Cancelamento')
    motivo = models.TextField(max_length=200)

    def __str__(self):
        return self.motivo

# Classe Inscrição
class Inscricao(models.Model):

    participante = models.ForeignKey(Participante, verbose_name=u'Participante')
    data_inscricao = models.DateField(u'Data de Inscrição')
    cancelado = models.BooleanField(default=False)

    #relacionamentos
    encontro = models.ForeignKey(Encontro, verbose_name=u'Encontro', default=None)
    cancelamento = models.ForeignKey(Cancelamento, verbose_name=u'Cancelamento')

    def __str__(self):
        return '%s - %s' % (self.participante.nome, self.data_inscricao)

# Classe Equipe
class Equipe(models.Model):

    nome = models.CharField(max_length=30)

    #relacionamentos
    membros = models.ManyToManyField(Lider)

    def __str__(self):
        return self.nome
