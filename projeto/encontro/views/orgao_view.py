# -*- coding: utf-8 -*-
import datetime

from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from django_tables2  import RequestConfig
from django.contrib import messages
from django.db import IntegrityError

from encontro.models import Orgao
from encontro.forms import OrgaoForm
from encontro.tables  import OrgaoTable
from usuario.views.usuario_views import entrar

#######################################################################################################################################################################
# Cadastro de Orgãos ##################################################################################################################################################
#######################################################################################################################################################################
@login_required(login_url=entrar)
def cadastrar_orgaos(request):
	# Se dados forem passados via POST
	table_orgao = OrgaoTable(Orgao.objects.order_by("nome"))
	RequestConfig(request, paginate={"per_page": 10}).configure(table_orgao)

	if request.method == 'POST':

		form = OrgaoForm(request.POST)

		if form.is_valid():

			nome = form.cleaned_data["nome"]

			alt_usuario_nome = '{}({})'.format(request.user.get_full_name(), request.user.email)
			alt_usuario_data = datetime.datetime.now()

			try:
	       		# cria um novo orgao
				orgao = Orgao.objects.create(nome=nome, alt_usuario_nome=alt_usuario_nome, alt_usuario_data=alt_usuario_data)
				orgao.save()

				table_orgao = OrgaoTable(Orgao.objects.order_by("nome"))
				RequestConfig(request, paginate={"per_page": 10}).configure(table_orgao)

				# faz a releitura da página
				messages.success(request, 'O orgão "{}" foi cadastrado com sucesso.'.format(orgao.nome))
				return render(request, "cadastrar_orgaos.html", {"form": OrgaoForm(), 'table_orgao': table_orgao})

			except IntegrityError:
				#Envia uma mensagem informando o erro de banco.
				messages.error(request, 'O nome "{}" já está sendo utilizado. Por favor, tente um nome diferente.'.format(nome))
				return render(request, "cadastrar_orgaos.html", {"form": OrgaoForm(), 'table_orgao': table_orgao})
		else:
			messages.warning(request, 'Desculpe, algo não funcionou como esperavamos... Tente novamente!')
			return render(request, "cadastrar_orgaos.html", {"form": OrgaoForm(), 'table_orgao': table_orgao})

	#se nenhuma informacao for passada, exibe a pagina com o formulário
	return render(request, "cadastrar_orgaos.html", {"form": OrgaoForm(), 'table_orgao': table_orgao})

#######################################################################################################################################################################
# Editar Orgãos #######################################################################################################################################################
#######################################################################################################################################################################
@login_required(login_url=entrar)
def editar_orgaos(request, id):
	# Se dados forem passados via POST
	table_orgao = OrgaoTable(Orgao.objects.order_by("nome"))
	RequestConfig(request, paginate={"per_page": 10}).configure(table_orgao)

	orgao = Orgao.objects.get(pk=id)

	if request.method == 'POST':

		form = OrgaoForm(request.POST, initial = {'nome': orgao.nome})

		if form.is_valid():

			nome = form.cleaned_data["nome"]

			alt_usuario_nome = '{}({})'.format(request.user.get_full_name(), request.user.email)
			alt_usuario_data = datetime.datetime.now()

			try:
				# atualiza os dados do orgao
				orgao.nome = nome

				orgao.alt_usuario_nome = alt_usuario_nome
				orgao.alt_usuario_data = alt_usuario_data

				orgao.save()

				table_orgao = OrgaoTable(Orgao.objects.order_by("nome"))
				RequestConfig(request, paginate={"per_page": 10}).configure(table_orgao)

				# faz a releitura da página
				messages.success(request, 'O orgão "{}" foi atualizado com sucesso.'.format(orgao.nome))
				return redirect('cadastrar_orgaos')

			except IntegrityError:
				#Envia uma mensagem informando o erro de banco.
				messages.error(request, 'O nome "{}" já está sendo utilizado. Por favor, tente um nome diferente.'.format(nome))
				return render(request, "cadastrar_orgaos.html", {"form": OrgaoForm(), 'table_orgao': table_orgao})
		else:
			messages.warning(request, 'Desculpe, algo não funcionou como esperavamos... Tente novamente!')
			return redirect('cadastrar_orgaos')

	#se nenhuma informacao for passada, exibe a pagina com o formulário
	return render(request, "cadastrar_orgaos.html", {"form": OrgaoForm(initial = {'nome': orgao.nome}), 'table_orgao': table_orgao})

#######################################################################################################################################################################
# Página de excluir Orgãos ############################################################################################################################################
#######################################################################################################################################################################
@login_required(login_url=entrar)
def excluir_orgaos(request, id):

	try:
		orgao = Orgao.objects.get(pk=id)
		orgao.delete()
	except Orgao.DoesNotExist:
		#Envia uma mensagem informando o erro de banco.
		messages.error(request, 'Esse orgao não encontra-se cadastrado em nossa base de dados.')
	return redirect('cadastrar_orgaos')
