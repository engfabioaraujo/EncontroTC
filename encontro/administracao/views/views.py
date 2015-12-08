from django.shortcuts import render

from django.contrib.auth.decorators import login_required

#Modelos de Dados do Projeto Encontro
from administracao.models import Lider, Orgao, Quarto
from .forms import LiderForm, OrgaoForm, QuartoForm

# Página de cadastro de Orgãos
@login_required(login_url='/usuario/')
def cadastro_orgao(request):
	# Se dados forem passados via POST	
	if request.method == 'POST':

		form = OrgaoForm(request.POST)

		if form.is_valid():

			nome = request.POST["nome"]

			# cria um novo grupo de usuarios
			orgao = Orgao.objects.create(nome=nome)
			orgao.save()

			# faz a releitura da página
			return render(request, "cadastrar_orgaos.html", {"form": OrgaoForm(), "lista_orgaos": Orgao.objects.all()})			

		else:
			return render(request, "cadastrar_orgaos.html", {"form": OrgaoForm(), "lista_orgaos": Orgao.objects.all()})			

	#se nenhuma informacao for passada, exibe a pagina com o formulário	
	return render(request, "cadastrar_orgaos.html", {"form": OrgaoForm(), "lista_orgaos": Orgao.objects.all()})	    

# Página de cadastro de Quartos
@login_required(login_url='/usuario/')
def cadastro_quarto(request):
	# Se dados forem passados via POST	
	if request.method == 'POST':

		form = QuartoForm(request.POST)

		if form.is_valid():

			nome = request.POST["nome"]
			lider = request.POST["lider"]

			# cria um novo grupo de usuarios
			quarto = Quarto.objects.create(nome=nome, lider=lider)
			quarto.save()

			# faz a releitura da página
			return render(request, "cadastrar_quartos.html", {"form": QuartoForm(), "lista_quartos": Quarto.objects.all()})			

		else:
			return render(request, "cadastrar_quartos.html", {"form": QuartoForm(), "lista_quartos": Quarto.objects.all()})			

	#se nenhuma informacao for passada, exibe a pagina com o formulário	
	return render(request, "cadastrar_quartos.html", {"form": QuartoForm(), "lista_quartos": Quarto.objects.all()})	    

# Página de cadastro de Líderes
@login_required(login_url='/usuario/')
def cadastro_lider(request):
	# Se dados forem passados via POST	
	if request.method == 'POST':

		form = LiderForm(request.POST, request.FILES)

		if form.is_valid():
			
			nome = request.POST['nome']
			sobrenome = request.POST['sobrenome']
			telefone = request.POST['telefone']
			email = request.POST['email']
			sexo = request.POST['sexo']
			data_nascimento = request.POST['data_nascimento']
			cargo = request.POST['cargo']						

			# cria um novo líder
			lider = Lider.objects.create(nome=nome, sobrenome=sobrenome, telefone=telefone, email=email, sexo=sexo, data_nascimento=data_nascimento, cargo=cargo)
			lider.foto.save("foto_" + str(lider.pk) + '_lider.jpg', request.FILES['foto'], save=False)
			lider.save()									

			# faz a releitura da página
			return render(request, "cadastro_lider.html", {"form": LiderForm(), "lista_lider": Lider.objects.all()})
			
		else:
			return render(request, "cadastro_lider.html", {"form": LiderForm(), "lista_lider": Lider.objects.all()})

	#se nenhuma informacao for passada, exibe a pagina com o formulário
	return render(request, "cadastro_lider.html", {"form": LiderForm(), "lista_lider": Lider.objects.all()})