# -*- coding: utf-8 -*-
import datetime

from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from django_tables2  import RequestConfig
from django.contrib import messages
from django.db import IntegrityError

from encontro.models import Encontro, Lider, Quarto, ResponsavelQuarto
from encontro.forms import QuartoCadastrarForm, QuartoEditarForm
from encontro.tables  import QuartoTable, QuartoResponsavelTable
from usuario.views.usuario_views import entrar

#######################################################################################################################################################################
# Página de cadastro de Quartos #######################################################################################################################################
#######################################################################################################################################################################
@login_required(login_url=entrar)
def cadastrar_quartos(request):
	# Se dados forem passados via POST
	encontro = Encontro.objects.get(ativo=True)
	table_quarto = QuartoTable(Quarto.objects.filter(encontro=encontro.pk).order_by("nome"))
	RequestConfig(request, paginate={"per_page": 10}).configure(table_quarto)

	if request.method == 'POST':

		form = QuartoCadastrarForm(request.POST)

		if form.is_valid():

			nome = form.cleaned_data["nome"]

			alt_usuario_nome = '{}({})'.format(request.user.get_full_name(), request.user.email)
			alt_usuario_data = datetime.datetime.now()

			try:
	       		# cria um novo quarto
				quarto = Quarto.objects.create(nome=nome, encontro=encontro, alt_usuario_nome=alt_usuario_nome, alt_usuario_data=alt_usuario_data)
				quarto.save()

				table_quarto = QuartoTable(Quarto.objects.order_by("nome"))
				RequestConfig(request, paginate={"per_page": 10}).configure(table_quarto)

				# faz a releitura da página
				messages.success(request, 'O quarto "{}" foi cadastrado com sucesso.'.format(quarto.nome))
				return render(request, "cadastrar_quartos.html", {"form": QuartoCadastrarForm(), 'table_quarto': table_quarto})

			except IntegrityError:
				#Envia uma mensagem informando o erro de banco.
				messages.error(request, 'O nome "{}" já está sendo utilizado. Por favor, tente um nome de quarto diferente para este encontro.'.format(nome))
				return render(request, "cadastrar_quartos.html", {"form": QuartoCadastrarForm(), 'table_quarto': table_quarto})
		else:
			messages.warning(request, 'Desculpe, algo não funcionou como esperavamos... Tente novamente!')
			return render(request, "cadastrar_quartos.html", {"form": QuartoCadastrarForm(), 'table_quarto': table_quarto})

	#se nenhuma informacao for passada, exibe a pagina com o formulário
	return render(request, "cadastrar_quartos.html", {"form": QuartoCadastrarForm(), 'table_quarto': table_quarto})

#######################################################################################################################################################################
# Editar Quartos ######################################################################################################################################################
#######################################################################################################################################################################
@login_required(login_url=entrar)
def editar_quartos(request, id):
	# Se dados forem passados via POST
	quarto = Quarto.objects.get(pk=id)

	#Cria lista de responsaveis_quarto
	responsaveis = list(quarto.responsaveis.order_by("nome"))
	responsaveis_quarto = []
	i = 0
	while i < len(responsaveis):
		responsavel = responsaveis[i]
		responsaveis_quarto.append(ResponsavelQuarto(quarto.id, responsavel.id, responsavel.get_nome_completo(), responsavel.telefone, responsavel.email))
		i = i + 1

	#Cria tabela de responsaveis por quarto
	#table_quarto_responsaveis = QuartoResponsavelTable(quarto.responsaveis.order_by("nome"))
	table_quarto_responsaveis = QuartoResponsavelTable(responsaveis_quarto)
	RequestConfig(request, paginate={"per_page": 10}).configure(table_quarto_responsaveis)

	if request.method == 'POST':
		form = QuartoEditarForm(request.POST, initial = {'nome': quarto.nome})

		if form.is_valid():

			nome = form.cleaned_data["nome"]
			responsavel = form.cleaned_data["responsavel"]

			alt_usuario_nome = '{}({})'.format(request.user.get_full_name(), request.user.email)
			alt_usuario_data = datetime.datetime.now()

			try:
				# atualiza os dados do orgao
				quarto.nome = nome

				quarto.alt_usuario_nome = alt_usuario_nome
				quarto.alt_usuario_data = alt_usuario_data
				quarto.save()

				quarto.responsaveis.add(responsavel)
				quarto.save()

				table_quarto_responsaveis = QuartoResponsavelTable(quarto.responsaveis.order_by("nome"))
				RequestConfig(request, paginate={"per_page": 10}).configure(table_quarto_responsaveis)

				# faz a releitura da página
				messages.success(request, 'O quarto "{}" foi atualizado com sucesso.'.format(quarto.nome))
				return redirect('editar_quartos', id=quarto.id)

			except IntegrityError:
				#Envia uma mensagem informando o erro de banco.
				messages.error(request, 'Esse responsável "{}" já foi cadastrado. Por favor, tente um nome diferente.'.format(nome))
				return render(request, "editar_quartos.html", {"form": QuartoEditarForm(), 'table_quarto_responsaveis': table_quarto_responsaveis})

		else:
			messages.warning(request, 'Desculpe, algo não funcionou como esperavamos... Tente novamente!')
			return redirect('editar_quartos', id=quarto.id)

	#se nenhuma informacao for passada, exibe a pagina com o formulário
	return render(request, "editar_quartos.html", {"form": QuartoEditarForm(initial = {'nome': quarto.nome}), 'table_quarto_responsaveis': table_quarto_responsaveis})

#######################################################################################################################################################################
# Excluir Quartos #####################################################################################################################################################
#######################################################################################################################################################################
@login_required(login_url=entrar)
def excluir_quartos(request, id):
	try:
		quarto = Quarto.objects.get(pk=id)
		quarto.delete()
	except Quarto.DoesNotExist:
		#Envia uma mensagem informando o erro de banco.
		messages.error(request, 'Esse quarto não encontra-se cadastrado em nossa base de dados.')
	return redirect('cadastrar_quartos')

#######################################################################################################################################################################
# Excluir Responsável de Quartos ######################################################################################################################################
#######################################################################################################################################################################
@login_required(login_url=entrar)
def excluir_responsaveis_quarto(request, idq, idr):
	try:
		quarto = Quarto.objects.get(pk=idq)
		responsavel = Lider.objects.get(pk=idr)
		quarto.responsaveis.remove(responsavel)
		quarto.save()
	except Quarto.DoesNotExist:
		#Envia uma mensagem informando o erro de banco.
		messages.error(request, 'Esse quarto não encontra-se cadastrado em nossa base de dados.')
	return redirect('editar_quartos', id=idq)
