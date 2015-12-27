# -*- coding: utf-8 -*-
import time
from datetime import date

from django import forms
from django.forms import extras
from django.contrib.admin.widgets import FilteredSelectMultiple

from encontro.models import Lider

#######################################################################################################################################################################
#Formulário para Cadastrar e Editar Orgãos ############################################################################################################################
#######################################################################################################################################################################
class OrgaoForm(forms.Form):

	nome = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'id': 'nome', 'class': 'form-control', 'name': 'nome', 'required': True}))

#######################################################################################################################################################################
#Formulário para Cadastrar Encontro de Jovens #########################################################################################################################
#######################################################################################################################################################################
class EncontroForm(forms.Form):

	ano    = forms.IntegerField(max_value=(date.today().year + 15), min_value=(date.today().year - 15), widget=forms.NumberInput(attrs={'id': 'ano', 'class': 'form-control', 'name': 'ano', 'required': True}))
	tema   = forms.CharField(max_length=500, min_length=10, widget=forms.Textarea(attrs={'id': 'tema', 'class': 'form-control', 'name': 'tema', 'required': True, 'autofocus': 'autofocus', 'style': 'height:100px;'}))
	vagas  = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'vagas', 'class': 'form-control', 'name': 'vagas', 'required': True}))
	valor  = forms.FloatField(widget=forms.NumberInput(attrs={'id': 'valor', 'class': 'form-control', 'name': 'valor', 'required': True}))

#######################################################################################################################################################################
#Formulário para Cadastrar e Editar Líder #############################################################################################################################
#######################################################################################################################################################################
class LiderForm(forms.Form):

	#Tipos de Sexo
	CHOICES_SEXO = (('M', 'Masculino'), ('F', 'Feminino'))
	#Tipo de Cargo
	CHOICES_CARGO = (('Membro', 'Membro'),
                     ('Auxíliar', 'Auxíliar'),
                     ('Diácono' , 'Diácono'),
                     ('Presbítero', 'Presbítero'),
                     ('Evangelísta', 'Evangelísta'),
					 ('Pastor', 'Pastor'))

	nome = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'id': 'nome', 'class': 'form-control', 'name': 'nome', 'required': True}))
	sobrenome = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'id': 'sobrenome', 'class': 'form-control', 'name': 'sobrenome', 'required': True}))
	telefone = forms.CharField(max_length=13, widget=forms.TextInput(attrs={'id': 'telefone', 'class': 'form-control', 'name': 'telefone', 'required': True}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'email', 'class': 'form-control', 'name': 'email', 'required': True}))
	sexo = forms.ChoiceField(choices=CHOICES_SEXO, widget=forms.Select(attrs={'id': 'sexo', 'class': 'form-control m-bot15', 'name': 'sexo', 'required': True}))

	data_nascimento = forms.DateField(initial=date.today(), widget=extras.SelectDateWidget(years=range(date.today().year, 1970, -1), attrs={'id': 'data_nascimento', 'class': 'form-control', 'name': 'data_nascimento', 'required': False}))

	cargo = forms.ChoiceField(choices=CHOICES_CARGO, widget=forms.Select(attrs={'id': 'cargo', 'class': 'form-control', 'name': 'cargo', 'required': True}))
	foto = forms.ImageField(label='Selecione a Foto...', widget=forms.FileInput(attrs={'id': 'foto', 'class': 'form-control', 'name': 'foto', 'style': "display:none", 'required': True}))

#######################################################################################################################################################################
#Formulário para Cadastrar e Editar Quarto ############################################################################################################################
#######################################################################################################################################################################
class QuartoForm(forms.Form):

	nome = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'id': 'nome', 'class': 'form-control', 'name': 'nome', 'required': True}))
	responsavel = forms.ChoiceField(choices=[ (l.id, l.nome) for l in Lider.objects.all()], widget=forms.Select(attrs={'id': 'responsavel', 'class': 'form-control m-bot15', 'name': 'responsavel', 'required': True}))
	responsaveis = forms.ModelMultipleChoiceField(queryset=Lider.objects.all(), widget=FilteredSelectMultiple(verbose_name='Lider', is_stacked=False, attrs={'id': 'responsaveis', 'class': 'form-control m-bot15', 'name': 'responsaveis'}))

'''
	def __init__(self, *args, **kwargs):
		super(QuartoForm, self).__init__(*args, **kwargs)
		if self.pk:
			self.fields['responsaveis'].initial = self.responsaveis.all()
'''
