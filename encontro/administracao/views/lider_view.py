# -*- coding: utf-8 -*-
import datetime

from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from django_tables2  import RequestConfig

from django.contrib import messages
from django.db import IntegrityError

from administracao.models import Lider
from administracao.forms import LiderForm
from administracao.tables  import LiderTable
from usuario.usuario_views import entrar

# Página de cadastro de Líderes
@login_required(login_url=entrar)
def cadastrar_lider(request):
	# Se dados forem passados via POST
	table_lider = LiderTable(Lider.objects.order_by("nome"))
	RequestConfig(request, paginate={"per_page": 10}).configure(table_lider)

	if request.method == 'POST':

		form = LiderForm(request.POST, request.FILES)

		#2015-12-22
		data = dict(request.POST)["data_nascimento"]
		ano = data[2]
		mes = data[1]
		dia = data[0]
		request.POST["data_nascimento"] = '{}-{}-{}'.format(ano, mes, dia)

		if form.is_valid():

			nome = form.cleaned_data["nome"]
			sobrenome = form.cleaned_data["sobrenome"]
			telefone = form.cleaned_data["telefone"]
			email = form.cleaned_data["email"]
			sexo = form.cleaned_data["sexo"]
			data_nascimento = form.cleaned_data["data_nascimento"]
			cargo = form.cleaned_data["cargo"]

			alt_usuario_nome = '{}({})'.format(request.user.get_full_name(), request.user.email)
			alt_usuario_data = datetime.datetime.now()

			try:
	       		# cria um novo lider
				lider = Lider.objects.create(nome=nome, sobrenome=sobrenome, telefone=telefone, email=email, sexo=sexo,
											 data_nascimento=data_nascimento, cargo=cargo, alt_usuario_nome=alt_usuario_nome, alt_usuario_data=alt_usuario_data)

				lider.foto.save("foto_" + str(lider.nome) + "_" + str(lider.sobrenome) + "_" + str(lider.telefone) + "_lider.jpg", request.FILES['foto'], save=False)
				lider.save()

				table_lider = LiderTable(Lider.objects.order_by("nome"))
				RequestConfig(request, paginate={"per_page": 10}).configure(table_lider)

				# faz a releitura da página
				messages.success(request, 'O líder "{}" foi cadastrado com sucesso.'.format(lider.get_nome_completo()))
				return render(request, "cadastrar_lider.html", {"form": LiderForm(), 'table_lider': table_lider})

			except IntegrityError:
				#Envia uma mensagem informando o erro de banco.
				messages.error(request, 'O email "{}" já está sendo utilizado. Por favor, tente um email diferente.'.format(email))
				return render(request, "cadastrar_lider.html", {"form": LiderForm(), 'table_lider': table_lider})
		else:
			messages.warning(request, 'Desculpe, algo não funcionou como esperavamos... Tente novamente!')
			return render(request, "cadastrar_lider.html", {"form": LiderForm(), 'table_lider': table_lider})

	#se nenhuma informacao for passada, exibe a pagina com o formulário
	return render(request, "cadastrar_lider.html", {"form": LiderForm(), 'table_lider': table_lider})


# Página de editar Líderes
@login_required(login_url=entrar)
def editar_lider(request, id):
	# Se dados forem passados via POST
	table_lider = LiderTable(Lider.objects.order_by("nome"))
	RequestConfig(request, paginate={"per_page": 10}).configure(table_lider)

	lider = Lider.objects.get(pk=id)

	if request.method == 'POST':

		#2015-12-22
		data = dict(request.POST)["data_nascimento"]
		ano = data[2]
		mes = data[1]
		dia = data[0]
		request.POST["data_nascimento"] = '{}-{}-{}'.format(ano, mes, dia)

		form = LiderForm(request.POST, request.FILES, initial = {'nome': lider.nome, 'sobrenome': lider.sobrenome, 'telefone': lider.telefone, 'email': lider.email,
			'sexo': lider.sexo,	'data_nascimento': lider.data_nascimento, 'cargo': lider.cargo})

		if form.is_valid():

			nome = form.cleaned_data["nome"]
			sobrenome = form.cleaned_data["sobrenome"]
			telefone = form.cleaned_data["telefone"]
			email = form.cleaned_data["email"]
			sexo = form.cleaned_data["sexo"]
			data_nascimento = form.cleaned_data["data_nascimento"]
			cargo = form.cleaned_data["cargo"]

			alt_usuario_nome = '{}({})'.format(request.user.get_full_name(), request.user.email)
			alt_usuario_data = datetime.datetime.now()

			try:
				# atualiza os dados do lider
				lider.nome = nome
				lider.sobrenome = sobrenome
				lider.telefone = telefone
				lider.email = email
				lider.sexo = sexo
				lider.data_nascimento = data_nascimento
				lider.cargo = cargo

				lider.alt_usuario_nome = alt_usuario_nome
				lider.alt_usuario_data = alt_usuario_data

				# lider.foto = request.FILES['foto']
				if request.FILES['foto']:
					lider.foto.delete(save=False)
					lider.foto.save("foto_" + str(lider.nome) + "_" + str(lider.sobrenome) + "_" + str(lider.telefone) + "_lider.jpg", request.FILES['foto'], save=False)

				lider.save()

				table_lider = LiderTable(Lider.objects.order_by("nome"))
				RequestConfig(request, paginate={"per_page": 10}).configure(table_lider)

				# faz a releitura da página
				messages.success(request, 'O Líder "{}" foi atualizado com sucesso.'.format(lider.get_nome_completo()))
				return redirect('cadastrar_lider')

			except IntegrityError:
				#Envia uma mensagem informando o erro de banco.
				messages.error(request, 'O email "{}" já está sendo utilizado. Por favor, tente um nome diferente.'.format(email))
				return render(request, "cadastrar_lider.html", {"form": LiderForm(), 'table_lider': table_lider})
		else:
			messages.warning(request, 'Desculpe, algo não funcionou como esperavamos... Tente novamente!')
			return redirect('cadastrar_lider')

	#se nenhuma informacao for passada, exibe a pagina com o formulário
	return render(request, "cadastrar_lider.html", {"form": LiderForm(initial = {'nome': lider.nome, 'sobrenome': lider.sobrenome, 'telefone': lider.telefone, 'email': lider.email, 'sexo': lider.sexo, 'data_nascimento': lider.data_nascimento, 'cargo': lider.cargo}), 'table_lider': table_lider})


# Página de excluir Líderes
@login_required(login_url=entrar)
def excluir_lider(request, id):
	try:
		lider = Lider.objects.get(pk=id)
		lider.delete()
	except Lider.DoesNotExist:
		#Envia uma mensagem informando o erro de banco.
		messages.error(request, 'Esse líder não encontra-se cadastrado em nossa base de dados.')
	return redirect('cadastrar_lider')
