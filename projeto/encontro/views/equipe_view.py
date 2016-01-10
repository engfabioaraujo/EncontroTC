# -*- coding: utf-8 -*-
import datetime

from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from django_tables2  import RequestConfig
from django.contrib import messages
from django.db import IntegrityError

from encontro.models import Encontro, Lider, Equipe, ComponenteEquipe
from encontro.forms import EquipeCadastrarForm, EquipeEditarForm
from encontro.tables  import EquipeTable, EquipeComponenteTable
from usuario.views.usuario_views import entrar

#######################################################################################################################################################################
# Página de cadastro de Equipes #######################################################################################################################################
#######################################################################################################################################################################
@login_required(login_url=entrar)
def cadastrar_equipes(request):
	# Se dados forem passados via POST
	encontro = Encontro.objects.get(ativo=True)
	table_equipe = EquipeTable(Equipe.objects.filter(encontro=encontro.pk).order_by("nome"))
	RequestConfig(request, paginate={"per_page": 10}).configure(table_equipe)

	if request.method == 'POST':

		form = EquipeCadastrarForm(request.POST)

		if form.is_valid():

			nome = form.cleaned_data["nome"]

			alt_usuario_nome = '{}({})'.format(request.user.get_full_name(), request.user.email)
			alt_usuario_data = datetime.datetime.now()

			try:
	       		# cria um novo equipe
				equipe = Equipe.objects.create(nome=nome, encontro=encontro, alt_usuario_nome=alt_usuario_nome, alt_usuario_data=alt_usuario_data)
				equipe.save()

				table_equipe = EquipeTable(Equipe.objects.order_by("nome"))
				RequestConfig(request, paginate={"per_page": 10}).configure(table_equipe)

				# faz a releitura da página
				messages.success(request, 'A equipe "{}" foi cadastrada com sucesso.'.format(equipe.nome))
				return render(request, "cadastrar_equipes.html", {"form": EquipeCadastrarForm(), 'table_equipe': table_equipe})

			except IntegrityError:
				#Envia uma mensagem informando o erro de banco.
				messages.error(request, 'O nome "{}" já está sendo utilizado. Por favor, tente um nome de equipe diferente para este encontro.'.format(nome))
				return render(request, "cadastrar_equipes.html", {"form": EquipeCadastrarForm(), 'table_equipe': table_equipe})
		else:
			messages.warning(request, 'Desculpe, algo não funcionou como esperavamos... Tente novamente!')
			return render(request, "cadastrar_equipes.html", {"form": EquipeCadastrarForm(), 'table_equipe': table_equipe})

	#se nenhuma informacao for passada, exibe a pagina com o formulário
	return render(request, "cadastrar_equipes.html", {"form": EquipeCadastrarForm(), 'table_equipe': table_equipe})

#######################################################################################################################################################################
# Editar Equipes ######################################################################################################################################################
#######################################################################################################################################################################
@login_required(login_url=entrar)
def editar_equipes(request, id):
	# Se dados forem passados via POST
	equipe = Equipe.objects.get(pk=id)

	#Cria lista de componentes_equipe
	componentes = list(equipe.componentes.order_by("nome"))
	componentes_equipe = []
	i = 0
	while i < len(componentes):
		componente = componentes[i]
		componentes_equipe.append(ComponenteEquipe(equipe.id, componente.id, componente.get_nome_completo(), componente.telefone, componente.email))
		i = i + 1

	#Cria tabela de componentes por equipe
	table_equipe_componentes = EquipeComponenteTable(componentes_equipe)
	RequestConfig(request, paginate={"per_page": 10}).configure(table_equipe_componentes)

	if request.method == 'POST':
		form = EquipeEditarForm(request.POST, initial = {'nome': equipe.nome})

		if form.is_valid():

			nome = form.cleaned_data["nome"]
			componente = form.cleaned_data["componente"]

			alt_usuario_nome = '{}({})'.format(request.user.get_full_name(), request.user.email)
			alt_usuario_data = datetime.datetime.now()

			try:
				# atualiza os dados do orgao
				equipe.nome = nome

				equipe.alt_usuario_nome = alt_usuario_nome
				equipe.alt_usuario_data = alt_usuario_data
				equipe.save()

				equipe.componentes.add(componente)
				equipe.save()

				table_equipe_componentes = EquipeComponenteTable(equipe.componentes.order_by("nome"))
				RequestConfig(request, paginate={"per_page": 10}).configure(table_equipe_componentes)

				# faz a releitura da página
				messages.success(request, 'A equipe "{}" foi atualizada com sucesso.'.format(equipe.nome))
				return redirect('editar_equipes', id=equipe.id)

			except IntegrityError:
				#Envia uma mensagem informando o erro de banco.
				messages.error(request, 'Esse componente "{}" já foi cadastrado. Por favor, tente um nome diferente.'.format(nome))
				return render(request, "editar_equipes.html", {"form": EquipeEditarForm(), 'table_equipe_componentes': table_equipe_componentes})

		else:
			messages.warning(request, 'Desculpe, algo não funcionou como esperavamos... Tente novamente!')
			return redirect('editar_equipes', id=equipe.id)

	#se nenhuma informacao for passada, exibe a pagina com o formulário
	return render(request, "editar_equipes.html", {"form": EquipeEditarForm(initial = {'nome': equipe.nome}), 'table_equipe_componentes': table_equipe_componentes})

#######################################################################################################################################################################
# Excluir Equipes #####################################################################################################################################################
#######################################################################################################################################################################
@login_required(login_url=entrar)
def excluir_equipes(request, id):
	try:
		equipe = Equipe.objects.get(pk=id)
		equipe.delete()
	except Equipe.DoesNotExist:
		#Envia uma mensagem informando o erro de banco.
		messages.error(request, 'Essa equipe não encontra-se cadastrada em nossa base de dados.')
	return redirect('cadastrar_equipes')

#######################################################################################################################################################################
# Excluir Responsável de Equipes ######################################################################################################################################
#######################################################################################################################################################################
@login_required(login_url=entrar)
def excluir_componentes_equipe(request, ide, idc):
	try:
		equipe = Equipe.objects.get(pk=ide)
		componente = Lider.objects.get(pk=idc)
		equipe.componentes.remove(componente)
		equipe.save()
	except Equipe.DoesNotExist:
		#Envia uma mensagem informando o erro de banco.
		messages.error(request, 'Essa equipe não encontra-se cadastrada em nossa base de dados.')
	return redirect('editar_equipes', id=ide)
