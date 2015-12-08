from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import Group
from .forms import CadastrarGruposForm

from usuario.tables  import GroupTable
from usuario.usuario_views import entrar

from django_tables2  import RequestConfig

from django.contrib import messages

from django.db import IntegrityError

# Página de cadastro de Grupos de Usuários
@login_required(login_url=entrar)
def cadastrar_grupos(request):
	# Se dados forem passados via POST	
	table_grupo = GroupTable(Group.objects.order_by("name"))
	RequestConfig(request, paginate={"per_page": 10}).configure(table_grupo)			

	if request.method == 'POST':

		form = CadastrarGruposForm(request.POST)

		if form.is_valid():
			
			nome = form.cleaned_data["nome"]

			try:							
	       		# cria um novo grupo de usuarios
				grupo = Group.objects.create(name=nome)
				grupo.save()	    		

				table_grupo = GroupTable(Group.objects.order_by("name"))
				RequestConfig(request, paginate={"per_page": 10}).configure(table_grupo)	

				# faz a releitura da página			
				messages.success(request, 'O grupo de usuário "{}" foi cadastrado com sucesso.'.format(grupo.name))
				return render(request, "cadastrar_grupos.html", {"form": CadastrarGruposForm(), 'table_grupo': table_grupo})			

			except IntegrityError:
				#Envia uma mensagem informando o erro de banco.				
				messages.error(request, 'o nome "{}" já está sendo utilizado. Por favor, tente um nome diferente.'.format(nome))
				return render(request, "cadastrar_grupos.html", {"form": CadastrarGruposForm(), 'table_grupo': table_grupo})				    		
		else:			
			messages.warning(request, 'Desculpe, algo não funcionou como esperavamos... Tente novamente!')
			return render(request, "cadastrar_grupos.html", {"form": CadastrarGruposForm(), 'table_grupo': table_grupo})				

	#se nenhuma informacao for passada, exibe a pagina com o formulário		
	return render(request, "cadastrar_grupos.html", {"form": CadastrarGruposForm(), 'table_grupo': table_grupo})			
	

# Página de editar Grupos de Usuários
@login_required(login_url=entrar)
def editar_grupos(request, id):
	# Se dados forem passados via POST	
	table_grupo = GroupTable(Group.objects.order_by("name"))
	RequestConfig(request, paginate={"per_page": 10}).configure(table_grupo)	

	grupo = Group.objects.get(pk=id)		
	
	if request.method == 'POST':

		form = CadastrarGruposForm(request.POST, initial = {'nome': grupo.name})

		if form.is_valid():

			nome = form.cleaned_data["nome"]

			try:			
				# cria um novo grupo de usuarios
				grupo.name = nome
				grupo.save()

				table_grupo = GroupTable(Group.objects.order_by("name"))
				RequestConfig(request, paginate={"per_page": 10}).configure(table_grupo)	

				# faz a releitura da página		
				messages.success(request, 'O grupo de usuário "{}" foi atualizado com sucesso.'.format(grupo.name))				
				return redirect('cadastrar_grupos')

			except IntegrityError:
				#Envia uma mensagem informando o erro de banco.				
				messages.error(request, 'o nome "{}" já está sendo utilizado. Por favor, tente um nome diferente.'.format(nome))
				return render(request, "cadastrar_grupos.html", {"form": CadastrarGruposForm(), 'table_grupo': table_grupo})
		else:						
			return redirect('cadastrar_grupos')

	#se nenhuma informacao for passada, exibe a pagina com o formulário		
	return render(request, "cadastrar_grupos.html", {"form": CadastrarGruposForm(initial = {'nome': grupo.name}), 'table_grupo': table_grupo})			

# Página de excluir Grupos de Usuários
@login_required(login_url=entrar)
def excluir_grupos(request, id):
			
	try:			
		grupo = Group.objects.get(pk=id)
		grupo.delete()					
	except Group.DoesNotExist:
		#Envia uma mensagem informando o erro de banco.				
		messages.error(request, 'Esse grupo de usuário não encontra-se cadastrado em nossa base de dados.')
	return redirect('cadastrar_grupos')			