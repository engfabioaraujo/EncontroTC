# -*- coding: utf-8 -*-
import django_tables2 as tables

from django.utils.safestring import mark_safe
from django.utils.html import escape
from django.core.urlresolvers import reverse

from encontro.models import Orgao, Encontro, Lider
from encontro.models import Equipe, ComponenteEquipe
from encontro.models import Quarto, ResponsavelQuarto

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

		href_editar = reverse('editar_quartos', args=[str(value)])
		href_excluir = "new MyQuestion('Deseja realmente excluir esse registro?', '{}').question()".format(reverse('excluir_quartos', args=[str(value)]))

		return mark_safe('<a href="%s">Editar</a> | <a href="javascript:func()" onclick="%s">Excluir</a>' % (escape(href_editar), escape(href_excluir)))

class QuartoTable(tables.Table):
	id = ControlQuartoColumn(verbose_name=" ", attrs={"th": {"style": "width: 120px;"}})
	nome = tables.Column(verbose_name="Nome")
	responsaveis = tables.Column(verbose_name="Responsáveis", accessor='get_responsaveis')

	class Meta:
		model = Quarto
		attrs = {"id": "tb_quartos", "class": "table table-striped table-advance table-hover"}
		fields = ("nome", "responsaveis", "id")

######################################################################################################################################################################
# Quarto - Responsáveis ##############################################################################################################################################
######################################################################################################################################################################
class ControlQuartoResponsavelColumn(tables.Column):
	def render(self, value):
		href_excluir_resp = "new MyQuestion('Deseja realmente excluir esse registro?', '{}').question()".format(reverse('excluir_responsaveis_quarto', args=[str(value[0]),str(value[1])]))
		return mark_safe('<a href="javascript:func()" onclick="%s">Excluir</a>' % (escape(href_excluir_resp)))

class QuartoResponsavelTable(tables.Table):
	responsavelquartoid = ControlQuartoResponsavelColumn(verbose_name=" ", attrs={"th": {"style": "width: 70px;"}})
	nome = tables.Column(verbose_name="Nome")
	telefone = tables.Column(verbose_name="Telefone")
	email = tables.Column(verbose_name="Email")

	class Meta:
		model = ResponsavelQuarto
		attrs = {"id": "tb_quarto_responsaveis", "class": "table table-striped table-advance table-hover"}
		fields = ("nome", "telefone", "email", "responsavelquartoid")

######################################################################################################################################################################
# Equipes ############################################################################################################################################################
######################################################################################################################################################################
class ControlEquipeColumn(tables.Column):
	def render(self, value):

		href_editar = reverse('editar_equipes', args=[str(value)])
		href_excluir = "new MyQuestion('Deseja realmente excluir esse registro?', '{}').question()".format(reverse('excluir_equipes', args=[str(value)]))

		return mark_safe('<a href="%s">Editar</a> | <a href="javascript:func()" onclick="%s">Excluir</a>' % (escape(href_editar), escape(href_excluir)))

class EquipeTable(tables.Table):
	id = ControlEquipeColumn(verbose_name=" ", attrs={"th": {"style": "width: 120px;"}})
	nome = tables.Column(verbose_name="Nome")
	componentes = tables.Column(verbose_name="Componentes", accessor='get_componentes')

	class Meta:
		model = Equipe
		attrs = {"id": "tb_equipes", "class": "table table-striped table-advance table-hover"}
		fields = ("nome", "componentes", "id")

######################################################################################################################################################################
# Equipe - Componentes ###############################################################################################################################################
######################################################################################################################################################################
class ControlEquipeComponenteColumn(tables.Column):
	def render(self, value):
		href_excluir_comp = "new MyQuestion('Deseja realmente excluir esse registro?', '{}').question()".format(reverse('excluir_componentes_equipe', args=[str(value[0]),str(value[1])]))
		return mark_safe('<a href="javascript:func()" onclick="%s">Excluir</a>' % (escape(href_excluir_comp)))

class EquipeComponenteTable(tables.Table):
	componente_equipe_id = ControlEquipeComponenteColumn(verbose_name=" ", attrs={"th": {"style": "width: 70px;"}})
	nome = tables.Column(verbose_name="Nome")
	telefone = tables.Column(verbose_name="Telefone")
	email = tables.Column(verbose_name="Email")

	class Meta:
		model = ComponenteEquipe
		attrs = {"id": "tb_equipe_componentes", "class": "table table-striped table-advance table-hover"}
		fields = ("nome", "telefone", "email", "componente_equipe_id")
