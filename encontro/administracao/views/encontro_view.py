# -*- coding: utf-8 -*-
import datetime

from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from django_tables2 import RequestConfig
from django.contrib import messages
from django.db import IntegrityError

from administracao.models import Encontro
from administracao.forms import EncontroForm
from administracao.tables import EncontroTable
from usuario.usuario_views import entrar


# Página de cadastro de Encontro de Jovens
@login_required(login_url=entrar)
def cadastrar_encontros(request):
    # Se dados forem passados via POST
    table_encontro = EncontroTable(Encontro.objects.order_by("-ano", "tema"))
    RequestConfig(request, paginate={"per_page": 10}).configure(table_encontro)

    if request.method == 'POST':

        form = EncontroForm(request.POST)

        if form.is_valid():

            ano = form.cleaned_data["ano"]
            tema = form.cleaned_data["tema"]
            vagas = form.cleaned_data["vagas"]
            valor = form.cleaned_data["valor"]
            ativo = form.cleaned_data["ativo"]

            alt_usuario_nome = '{}({})'.format(request.user.get_full_name(), request.user.email)
            alt_usuario_data = datetime.datetime.now()

            try:
                # cria um novo Encontro de Jovens
                encontro = Encontro.objects.create(ano=ano, tema=tema, vagas=vagas, valor=valor, ativo=ativo, alt_usuario_nome=alt_usuario_nome, alt_usuario_data=alt_usuario_data)
                encontro.save()

                table_encontro = EncontroTable(Encontro.objects.order_by("-ano", "tema"))
                RequestConfig(request, paginate={"per_page": 10}).configure(table_encontro)

                # faz a releitura da página
                messages.success(request, 'O Encontro de Jovens {} foi cadastrado com sucesso.'.format(encontro.ano))
                return render(request, "cadastrar_encontros.html", {"form": EncontroForm(), 'table_encontro': table_encontro})

            except IntegrityError:
                # Envia uma mensagem informando o erro de banco.
                messages.error(request, 'O Encontro de Jovens "{}" já foi cadastrado. Por favor, tente o cadastro em um ano diferente.'.format(ano))
                return render(request, "cadastrar_encontros.html", {"form": EncontroForm(), 'table_encontro': table_encontro})
        else:
            messages.warning(request, 'Desculpe, algo não funcionou como esperavamos... Tente novamente!')
            return render(request, "cadastrar_encontros.html", {"form": EncontroForm(), 'table_encontro': table_encontro})

    # se nenhuma informacao for passada, exibe a pagina com o formulário
    return render(request, "cadastrar_encontros.html", {"form": EncontroForm(), 'table_encontro': table_encontro})


# Página de editar Encontro de Jovens
@login_required(login_url=entrar)
def editar_encontros(request, id):
    # Se dados forem passados via POST
    table_encontro = EncontroTable(Encontro.objects.order_by("-ano", "tema"))
    RequestConfig(request, paginate={"per_page": 10}).configure(table_encontro)

    encontro = Encontro.objects.get(pk=id)

    if request.method == 'POST':

        form = EncontroForm(request.POST, initial={"ano": encontro.ano, "tema": encontro.tema, "vagas": encontro.vagas, "valor": encontro.valor, "ativo": encontro.ativo})

        if form.is_valid():

            ano = form.cleaned_data["ano"]
            tema = form.cleaned_data["tema"]
            vagas = form.cleaned_data["vagas"]
            valor = form.cleaned_data["valor"]
            ativo = form.cleaned_data["ativo"]

            alt_usuario_nome = '{}({})'.format(request.user.get_full_name(), request.user.email)
            alt_usuario_data = datetime.datetime.now()

            try:
                # cria um novo Encontro de Jovens
                encontro.ano = ano
                encontro.tema = tema
                encontro.vagas = vagas
                encontro.valor = valor
                encontro.ativo = ativo

                encontro.alt_usuario_nome = alt_usuario_nome
                encontro.alt_usuario_data = alt_usuario_data

                encontro.save()

                table_encontro = EncontroTable(Encontro.objects.order_by("-ano", "tema"))
                RequestConfig(request, paginate={"per_page": 10}).configure(table_encontro)

                # faz a releitura da página
                messages.success(request, 'O Encontro de Jovens {} foi atualizado com sucesso.'.format(encontro.ano))
                return redirect('cadastrar_encontros')

            except IntegrityError:
                # Envia uma mensagem informando o erro de banco.
                messages.error(request, 'O Encontro de Jovens "{}" já foi cadastrado. Por favor, tente o cadastro em um ano diferente.'.format(ano))
                return render(request, "cadastrar_encontros.html", {"form": EncontroForm(), 'table_encontro': table_encontro})
        else:
            messages.warning(request, 'Desculpe, algo não funcionou como esperavamos... Tente novamente!')
            return redirect('cadastrar_encontros')

    # se nenhuma informacao for passada, exibe a pagina com o formulário
    return render(request, "cadastrar_encontros.html", {"form": EncontroForm(initial={"ano": encontro.ano, "tema": encontro.tema, "vagas": encontro.vagas, "valor": encontro.valor, "ativo": encontro.ativo}), 'table_encontro': table_encontro})


# Página de ativar/desativar Encontro de Jovens
@login_required(login_url=entrar)
def ativar_encontros(request, id):

    try:
        encontro = Encontro.objects.get(pk=id)
        # encontro.delete()
    except Encontro.DoesNotExist:
        # Envia uma mensagem informando o erro de banco.
        messages.error(request, 'O Encontro de Jovens não encontra-se cadastrado em nossa base de dados.')
    return redirect('cadastrar_encontros')


# Página de excluir Encontro de Jovens
@login_required(login_url=entrar)
def excluir_encontros(request, id):

    try:
        encontro = Encontro.objects.get(pk=id)
        encontro.delete()
    except Encontro.DoesNotExist:
        # Envia uma mensagem informando o erro de banco.
        messages.error(request, 'O Encontro de Jovens não encontra-se cadastrado em nossa base de dados.')
    return redirect('cadastrar_encontros')
