from django.shortcuts import render

#Funcao redirecionamento de páginas
from django.shortcuts import redirect

from usuario.views import usuario_views


# Página Principal do Sistema
def index(request):
	if request.user.is_authenticated():
	    return render(request, "index.html")
	else:
	    #se usuário não estiver logado, exibe a pagina de login.
	    return redirect(usuario_views.entrar)
