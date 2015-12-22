# -*- coding: utf-8 -*-
import django_tables2 as tables

from django.utils.safestring import mark_safe
from django.utils.html import escape
from django.core.urlresolvers import reverse

from encontro.models import Orgao, Encontro, Lider

######################################################################################################################################################################
# Encontro de Jovens #################################################################################################################################################
######################################################################################################################################################################
class ControlEncontroColumn(tables.Column):
	def render(self, value):

		href_editar = reverse('editar_encontros', args=[str(value)])
		href_excluir = "new MyQuestion('Deseja realmente excluir esse registro?', '{}').question()".format(reverse('excluir_encontros', args=[str(value)]))
		href_ativar = reverse('ativar_encontros', args=[str(value)])

		return mark_safe('<a href="%s">Editar</a> | <a href="javascript:func()" onclick="%s">Excluir</a> | <a href="%s">Ativar Encontro</a>' % (escape(href_editar), escape(href_excluir), escape(href_ativar)))

class BolleanColumn(tables.Column):
	def render(self, value):
		if value:
			return mark_safe('SIM')
		else:
			return mark_safe('NÃO')

class EncontroTable(tables.Table):
	id = ControlEncontroColumn(verbose_name=" ", attrs={"th": {"style": "width: 7%;"}})

	ano   = tables.Column(verbose_name="Ano", attrs={"th": {"style": "width: 5%;"}})
	tema  = tables.Column(verbose_name="Tema", attrs={"th": {"style": "width: 50%;"}})
	vagas = tables.Column(verbose_name="Vagas", attrs={"th": {"style": "width: 5%;"}})
	valor = tables.Column(verbose_name="Valor da Inscrição", attrs={"th": {"style": "width: 8%;"}})
	ativo = BolleanColumn(verbose_name="Ativo", attrs={"th": {"style": "width: 8%;"}})

	class Meta:
		model = Orgao
		attrs = {"id": "tb_encontros", "class": "table table-striped table-advance table-hover"}
		fields = ("tema", "ano", "vagas", "valor", "ativo", "id")

######################################################################################################################################################################
# Orgãos #############################################################################################################################################################
######################################################################################################################################################################
class ControlOrgaoColumn(tables.Column):
	def render(self, value):

		href_editar = reverse('editar_orgaos', args=[str(value)])
		href_excluir = "new MyQuestion('Deseja realmente excluir esse registro?', '{}').question()".format(reverse('excluir_orgaos', args=[str(value)]))

		return mark_safe('<a href="%s">Editar</a> | <a href="javascript:func()" onclick="%s">Excluir</a>' % (escape(href_editar), escape(href_excluir)))

class OrgaoTable(tables.Table):
	id = ControlOrgaoColumn(verbose_name=" ", attrs={"th": {"style": "width: 120px;"}})
	nome = tables.Column(verbose_name="Nome")

	class Meta:
		model = Orgao
		attrs = {"id": "tb_orgaos", "class": "table table-striped table-advance table-hover"}
		fields = ("nome", "id")

######################################################################################################################################################################
# Líderes ############################################################################################################################################################
######################################################################################################################################################################
class ControlLiderColumn(tables.Column):
	def render(self, value):

		href_editar = reverse('editar_lider', args=[str(value)])
		href_excluir = "new MyQuestion('Deseja realmente excluir esse registro?', '{}').question()".format(reverse('excluir_lider', args=[str(value)]))

		return mark_safe('<a href="%s">Editar</a> | <a href="javascript:func()" onclick="%s">Excluir</a>' % (escape(href_editar), escape(href_excluir)))

class LiderTable(tables.Table):
	id = ControlLiderColumn(verbose_name=" ", attrs={"th": {"style": "width: 120px;"}})
	cargo = tables.Column(verbose_name="Posição na Igreja")
	nome = tables.Column(verbose_name="Nome", accessor='get_nome_completo')
	email = tables.Column(verbose_name="Email")
	telefone = tables.Column(verbose_name="Telefone")
	data_nascimento = tables.Column(verbose_name="Data de Nascimento")

	class Meta:
		model = Lider
		attrs = {"id": "tb_orgaos", "class": "table table-striped table-advance table-hover"}
		fields = ("cargo", "nome", "email", "telefone", "data_nascimento", "id")

######################################################################################################################################################################
# Quartos ############################################################################################################################################################
######################################################################################################################################################################
class ControlQuartoColumn(tables.Column):
	def render(self, value):

		href_editar = reverse('editar_quarto', args=[str(value)])
		href_excluir = "new MyQuestion('Deseja realmente excluir esse registro?', '{}').question()".format(reverse('excluir_quarto', args=[str(value)]))

		return mark_safe('<a href="%s">Editar</a> | <a href="javascript:func()" onclick="%s">Excluir</a>' % (escape(href_editar), escape(href_excluir)))

class QuartoTable(tables.Table):
	id = ControlLiderColumn(verbose_name=" ", attrs={"th": {"style": "width: 120px;"}})
	nome = tables.Column(verbose_name="Nome")
	lideres = tables.Column(verbose_name="Líderes", accessor='get_responsaveis')
	encontro = tables.Column(verbose_name="Encontro")

	class Meta:
		model = Lider
		attrs = {"id": "tb_quartos", "class": "table table-striped table-advance table-hover"}
		fields = ("nome", "lideres", "encontro", "id")
