# -*- coding: utf-8 -*-
from django.contrib.auth.models import Group

from django import forms

#Formulário para Cadastro de Usuários
class RegistrarUsuarioForm(forms.Form):

	nome = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'id': 'nome', 'class': 'form-control', 'name': 'nome', 'required': True})) 			#'value': {{ user.first_name }},
	sobrenome = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'id': 'sobrenome', 'class': 'form-control', 'name': 'sobrenome', 'required': True}))   #'value': {{ user.last_name }},
	email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'email', 'class': 'form-control', 'name': 'email', 'required': True})) 				#'value': {{ user.email }},
	grupos = forms.ChoiceField(choices=[ (g.id, g.name) for g in Group.objects.all()], widget=forms.Select(attrs={'id': 'grupos', 'class': 'form-control m-bot15', 'name': 'grupos', 'required': True}))

#Formulário para Edição do Perfil do Usuário
class EditarUsuarioForm(forms.Form):

	nome = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'id': 'nome', 'class': 'form-control', 'name': 'nome', 'required': True})) 			#'value': {{ user.first_name }},
	sobrenome = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'id': 'sobrenome', 'class': 'form-control', 'name': 'sobrenome', 'required': True}))   #'value': {{ user.last_name }},
	email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'email', 'class': 'form-control', 'name': 'email', 'required': True})) 				#'value': {{ user.email }},
	senha = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'id': 'senha', 'class': 'form-control', 'name': 'senha', 'required': True}))
	confirmar_senha = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'id': 'confirmar_senha', 'class': 'form-control', 'name': 'confirmar_senha', 'required': True}))
	foto = forms.ImageField(label='Selecione a sua Foto de Perfil...', widget=forms.FileInput(attrs={'id': 'foto', 'class': 'form-control', 'name': 'foto', 'style': "display:none", 'required': False}))

#Formulário para Cadastro de Grupos de Usuário
class CadastrarGruposForm(forms.Form):

	nome = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'id': 'nome', 'class': 'form-control', 'name': 'nome', 'required': True}))
