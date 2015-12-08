from django.shortcuts import render

from django.http import HttpResponse

#Funcao redirecionamento de páginas
from django.shortcuts import redirect

#Funções de autenticação de usuário
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#Modelo User padrão do Django
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from usuario.tables  import UsuarioTable
from usuario.models import UsuarioEncontro

from .forms import RegistrarUsuarioForm, EditarUsuarioForm, CadastrarGruposForm
import encontro.views

from django_tables2   import RequestConfig
from usuario.tables  import GroupTable

from django.contrib import messages
from django.db import IntegrityError

#######################################################################################################################################################################
# Página para Login de Usuário ########################################################################################################################################
#######################################################################################################################################################################
def entrar(request):
	if request.user.is_authenticated():
		return redirect(encontro.views.index)
	else:
		if request.method == 'POST':

		    usuario = request.POST["usuario"]
		    senha = request.POST['senha']
		    user = authenticate(username=usuario, password=senha)

		    if user is not None:
		        if user.is_active:
		    	    login(request, user)
		    	    return redirect(encontro.views.index)
		        else:
		    	    # Return a 'disabled account' error message
		    	    return HttpResponse("Return a 'disabled account' error message")
		    else:
		        # Return an 'invalid login' error message
		        return HttpResponse("Return an 'invalid login' error message")
		    
		#se nenhuma informacao for passada, exibe a pagina com o formulário de login
		return render(request, "login.html")

#######################################################################################################################################################################
# Logout de Usuários ##################################################################################################################################################
#######################################################################################################################################################################
@login_required(login_url=entrar)
def sair(request):
    if request.user.is_authenticated():
        logout(request)
        return redirect(entrar) 

#######################################################################################################################################################################
# Página de cadastro de usuário #######################################################################################################################################
#######################################################################################################################################################################
@login_required(login_url=entrar)
def registrar_usuario(request):
	# Se dados forem passados via POST	
	table_usuario = UsuarioTable(User.objects.order_by("first_name", "last_name"))
	RequestConfig(request, paginate={"per_page": 10}).configure(table_usuario)				

	if request.method == 'POST':

		form = RegistrarUsuarioForm(request.POST)

		if form.is_valid():

			nome = form.cleaned_data["nome"]
			sobrenome = form.cleaned_data["sobrenome"]
			email = form.cleaned_data["email"]
			grupoId = form.cleaned_data["grupos"]

			#username = email 
			usuario = email
			#senha padrão de cadastrado
			senha = "encontro123"
			confirmar_senha = "encontro123"

			try:							
			
				if senha == confirmar_senha:
					
					# cria um novo usuario
					user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome, last_name=sobrenome)
					
					user.groups.clear()
					grupo = Group.objects.get(pk=grupoId)		
					user.groups.add(grupo)

					user.save()

					table_usuario = UsuarioTable(User.objects.order_by("first_name", "last_name"))					
					RequestConfig(request, paginate={"per_page": 10}).configure(table_usuario)

					# faz a releitura da página
					messages.success(request, 'O usuário "{}" foi cadastrado com sucesso.'.format(user.get_full_name()))
					return render(request, "registrar_usuario.html", {"form": RegistrarUsuarioForm(), 'table_usuario': table_usuario})
				else:
					# mostra novamente o formulario de cadastro com os erros do formulario atual
					messages.error(request, 'O campo "confirmar senha" precisa ser igual ao campo "senha".')
					return render(request, "registrar_usuario.html", {"form": RegistrarUsuarioForm(), 'table_usuario': table_usuario})
			
			except IntegrityError:
				#Envia uma mensagem informando o erro de banco.				
				messages.error(request, 'o nome "{}" já está sendo utilizado. Por favor, tente um email diferente.'.format(email))
				return render(request, "registrar_usuario.html", {"form": RegistrarUsuarioForm(), 'table_usuario': table_usuario})				    		
		else:
			messages.warning(request, 'Desculpe, algo não funcionou como esperavamos... Tente novamente!')
			return render(request, "registrar_usuario.html", {"form": RegistrarUsuarioForm(), 'table_grupo': table_usuario})

	#se nenhuma informacao for passada, exibe a pagina com o formulário
	return render(request, "registrar_usuario.html", {"form": RegistrarUsuarioForm(), "table_usuario": table_usuario})

#######################################################################################################################################################################
# Página de edição de usuário #######################################################################################################################################
#######################################################################################################################################################################
@login_required(login_url=entrar)
def editar_usuario(request, id):
	# Se dados forem passados via POST	
	table_usuario = UsuarioTable(User.objects.order_by("first_name", "last_name"))
	RequestConfig(request, paginate={"per_page": 10}).configure(table_usuario)		

	user = User.objects.get(pk=id)					

	if request.method == 'POST':

		form = RegistrarUsuarioForm(request.POST, initial = {'nome': user.first_name, 'sobrenome': user.last_name, 'email': user.email, 'grupos': user.groups.all()[0].pk })			

		if form.is_valid():

			nome = form.cleaned_data["nome"]
			sobrenome = form.cleaned_data["sobrenome"]
			email = form.cleaned_data["email"]
			grupoId = form.cleaned_data["grupos"]

			#username = email 
			usuario = email			

			try:							
			
				# cria um novo usuario
				user.username=usuario
				user.email=email					
				user.first_name=nome
				user.last_name=sobrenome
				
				user.groups.clear()
				grupo = Group.objects.get(pk=grupoId)		
				user.groups.add(grupo)

				user.save()

				table_usuario = UsuarioTable(User.objects.order_by("first_name", "last_name"))					
				RequestConfig(request, paginate={"per_page": 10}).configure(table_usuario)

				# faz a releitura da página					
				messages.success(request, 'O usuário "{}" foi atualizado com sucesso.'.format(user.get_full_name()))					
				return redirect('cadastrar_usuario')		    		
			
			except IntegrityError:
				#Envia uma mensagem informando o erro de banco.				
				messages.error(request, 'o email "{}" já está sendo utilizado. Por favor, tente um email diferente.'.format(email))
				return render(request, "registrar_usuario.html", {"form": RegistrarUsuarioForm(), 'table_usuario': table_usuario})				    		
		else:
			messages.warning(request, 'Desculpe, algo não funcionou como esperavamos... Tente novamente!')
			return render(request, "registrar_usuario.html", {"form": RegistrarUsuarioForm(), 'table_grupo': table_usuario})

	#se nenhuma informacao for passada, exibe a pagina com o formulário	
	return render(request, "registrar_usuario.html", {"form": RegistrarUsuarioForm(initial = {'nome': user.first_name, 'sobrenome': user.last_name, 'email': user.email, 'grupos': user.groups.all()[0].pk }), "table_usuario": table_usuario})

#######################################################################################################################################################################
# Página de edição dos dados do usuário (Perfil) ######################################################################################################################
#######################################################################################################################################################################
@login_required(login_url=entrar)
def editar_perfil(request):

	user = request.user				

	# Se dados forem passados via POST	
	if request.method == 'POST':

		#form = EditarUsuarioForm(request.POST, request.FILES)
		form = EditarUsuarioForm(request.POST, request.FILES, initial = {'nome': user.first_name, 'sobrenome': user.last_name, 'email': user.email, 'senha': user.password, 'confirmar_senha': user.password })			

		if form.is_valid():
			
			nome = form.cleaned_data['nome']
			sobrenome = form.cleaned_data['sobrenome']
			email = form.cleaned_data['email']
			senha = form.cleaned_data['senha']
			confirmar_senha = form.cleaned_data['confirmar_senha']						

			try:

				if senha == confirmar_senha:

				    # Recupera o usuário Logado
				    user = request.user

				    # Recupera o perfil do Usuário			    
				    usuario_encontro = UsuarioEncontro.objects.get(pk=user.pk)

				    # Atualiza as informações do Usuário
				    user.first_name = nome
				    user.last_name  = sobrenome
				    user.email      = email
				    user.set_password(senha)	
				    user.save()					    

				    # Atualiza as informações do Perfil do Usuário
				    #usuario_encontro.foto = request.FILES['foto']
				    usuario_encontro.foto.save("foto_" + str(user.pk) + '_perfil.jpg', request.FILES['foto'], save=False)			    			    
				    usuario_encontro.save()				    
				    
				    # faz a releitura da página
				    messages.success(request, 'O usuário "{}" foi atualizado com sucesso.'.format(user.get_full_name()))					
				    return redirect('editar_perfil')
				else:
					# mostra novamente o formulario de cadastro com os erros do formulario atual
					messages.error(request, 'O campo "confirmar senha" precisa ser igual ao campo "senha".')
					return render(request, "editar_perfil.html", {"form": EditarUsuarioForm(initial = {'nome': user.first_name, 'sobrenome': user.last_name, 'email': user.email, 'senha': user.password, 'confirmar_senha': user.password }), "usuario": request.user, "perfil": UsuarioEncontro.objects.get(pk=request.user.pk)})

			except IntegrityError:
				#Envia uma mensagem informando o erro de banco.				
				messages.error(request, 'Erro no banco.') #o nome "{}" já está sendo utilizado. Por favor, tente um email diferente. .format(email)
				return render(request, "editar_perfil.html", {"form": EditarUsuarioForm(initial = {'nome': user.first_name, 'sobrenome': user.last_name, 'email': user.email, 'senha': user.password, 'confirmar_senha': user.password }), "usuario": request.user, "perfil": UsuarioEncontro.objects.get(pk=request.user.pk)})
		else:
			messages.warning(request, 'Desculpe, algo não funcionou como esperavamos... Tente novamente!')
			return render(request, "editar_perfil.html", {"form": EditarUsuarioForm(initial = {'nome': user.first_name, 'sobrenome': user.last_name, 'email': user.email, 'senha': user.password, 'confirmar_senha': user.password }), "usuario": request.user, "perfil": UsuarioEncontro.objects.get(pk=request.user.pk)})

	#se nenhuma informacao for passada, exibe a pagina com o formulário
	return render(request, "editar_perfil.html", {"form": EditarUsuarioForm(initial = {'nome': user.first_name, 'sobrenome': user.last_name, 'email': user.email, 'senha': user.password, 'confirmar_senha': user.password })	, "usuario": request.user, "perfil": UsuarioEncontro.objects.get(pk=request.user.pk)})

#######################################################################################################################################################################
# Página de excluir Usuários ##########################################################################################################################################
#######################################################################################################################################################################
@login_required(login_url=entrar)
def excluir_usuario(request, id):			
	try:					
		usuario = User.objects.get(pk=id)
		usuario.delete()					
	except User.DoesNotExist:
		#Envia uma mensagem informando o erro de banco.				
		messages.error(request, 'Esse usuário não encontra-se cadastrado em nossa base de dados.')
	return redirect('cadastrar_usuario')			

#######################################################################################################################################################################
# Página de resetar senha de Usuários #################################################################################################################################
#######################################################################################################################################################################
@login_required(login_url=entrar)
def resetar_senha(request, id):			
	try:							
		# Recupera o usuário Logado
	    usuario = User.objects.get(pk=id)	    
	    usuario.set_password("encontro123")	
	    
	    # Salvando as informações no Banco de Dados
	    usuario.save()				
	except User.DoesNotExist:
		#Envia uma mensagem informando o erro de banco.				
		messages.error(request, 'Esse usuário não encontra-se cadastrado em nossa base de dados.')

	messages.success(request, 'A senha do usuário foi reinicializada para "encontro123".')
	return redirect('cadastrar_usuario')			