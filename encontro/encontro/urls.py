from django.conf.urls import include, url
from django.contrib import admin

from . import views
from usuario import usuario_views, grupo_views
from administracao.views import orgao_view, encontro_view, lider_view

urlpatterns = [
    #Aplicações
    url(r'^admin/', include(admin.site.urls)),        

    #Projeto
    url(r'^$', views.index, name='index'),  

    #Usuarios
    url(r'^login$', usuario_views.entrar, name='entrar'),    							                               # Página de Login
    url(r'^cadastrar_usuario$', usuario_views.registrar_usuario, name='cadastrar_usuario'),    	         # Página de Registro de Usuário
    url(r'^editar_perfil$', usuario_views.editar_perfil, name='editar_perfil'),      			               # Página Editar informações do Usuário
    url(r'^editar_usuario/(?P<id>[0-9]+)/$', usuario_views.editar_usuario, name='editar_usuario'),       # Página Editar Usuário
    url(r'^excluir_usuario/(?P<id>[0-9]+)/$', usuario_views.excluir_usuario, name='excluir_usuario'),    # Página para Excluir Usuário  
    url(r'^resetar_senha/(?P<id>[0-9]+)/$', usuario_views.resetar_senha, name='resetar_senha'),          # Página para resetar senha de Usuário  
    url(r'^sair/$', usuario_views.sair, name='sair'), 									                                 # Página de Logout

    #Grupo de Usuarios
    url(r'^cadastrar_grupos$', grupo_views.cadastrar_grupos, name='cadastrar_grupos'),  				    # Página de Cadastro de Grupos de Usuário
    url(r'^editar_grupos/(?P<id>[0-9]+)/$', grupo_views.editar_grupos, name='editar_grupos'),    		# Página para Editar Grupos de Usuário  
    url(r'^excluir_grupos/(?P<id>[0-9]+)/$', grupo_views.excluir_grupos, name='excluir_grupos'),    # Página para Excluir Grupos de Usuário  

    #Encontro de Jovens
    url(r'^cadastrar_encontros$', encontro_view.cadastrar_encontros, name='cadastrar_encontros'),              # Página de Cadastro de Encontro de Jovens
    url(r'^editar_encontros/(?P<id>[0-9]+)/$', encontro_view.editar_encontros, name='editar_encontros'),       # Página para Editar Encontro de Jovens
    url(r'^ativar_encontros/(?P<id>[0-9]+)/$', encontro_view.ativar_encontros, name='ativar_encontros'),       # Página para Ativar/Desativar Encontro de Jovens
    url(r'^excluir_encontros/(?P<id>[0-9]+)/$', encontro_view.excluir_encontros, name='excluir_encontros'),    # Página para Excluir Encontro de Jovens

    #Orgãos
    url(r'^cadastrar_orgaos$', orgao_view.cadastrar_orgaos, name='cadastrar_orgaos'),              # Página de Cadastro de Orgãos
    url(r'^editar_orgaos/(?P<id>[0-9]+)/$', orgao_view.editar_orgaos, name='editar_orgaos'),       # Página para Editar Orgãos
    url(r'^excluir_orgaos/(?P<id>[0-9]+)/$', orgao_view.excluir_orgaos, name='excluir_orgaos'),    # Página para Excluir Orgãos    

    #Líderes
    url(r'^cadastrar_lider$', lider_view.cadastrar_lider, name='cadastrar_lider'),              # Página de Cadastro de Líderes
    url(r'^editar_lider/(?P<id>[0-9]+)/$', lider_view.editar_lider, name='editar_lider'),       # Página para Editar Líderes
    url(r'^excluir_lider/(?P<id>[0-9]+)/$', lider_view.excluir_lider, name='excluir_lider'),    # Página para Excluir Líderes    
]


#has_module_perms(package_name)
#email_user(subject, message, from_email=None, **kwargs)
#create_superuser(username, email, password, **extra_fields)
#has_perm(user_obj, perm, obj=None)

'''
<div class="form-group">
	<label class="col-lg-1 control-label">Nome</label>
      	<div class="col-lg-3">
	<input id="nome" type="text" class="form-control" name="nome" value="{{ usuario.first_name }}" required />
      	</div>
	<label class="col-lg-1 control-label">Sobrenome</label>
	<div class="col-lg-3">
  		<input id="sobrenome" type="text" class="form-control" name="sobrenome" value="{{ usuario.last_name }}" required />
	</div>
</div>						  	          							          
<div class="form-group">
	<label class="col-lg-1 control-label">Email</label>
	<div class="col-lg-7">
  		<input id="email" type="email" class="form-control" name="email" value="{{ usuario.email }}" required />
	</div>
</div>						          	
<div class="form-group">
	<label class="col-lg-1 control-label">Senha</label>
      	<div class="col-lg-3">
		<input id="senha" type="password" class="form-control" name="senha" required />
      	</div>
	<label class="col-lg-1 control-label">Confirmar Senha</label>
	<div class="col-lg-3">
  		<input id="confirmar_senha" type="password" class="form-control" name="confirmar_senha" required />
	</div>
</div>
<div class="form-group">
      	<label class="col-lg-1 control-label"></label>
	<div class="col-lg-3">
		<span class="btn btn-default btn-file"><span>Escolha sua foto de Perfil</span><input type="file" class="form-control" name="foto_usuario" /></span>
	</div>
</div>
'''

'''
messages.debug(request, '%s SQL statements were executed.' % count)
messages.info(request, 'Three credits remain in your account.')
messages.success(request, 'Profile details updated.')
messages.warning(request, 'Your account expires in three days.')
messages.error(request, 'Document deleted.')
'''

'''

<li class="sub-menu">
          <a href="javascript:;" class="">
              <i class="icon_desktop"></i>
              <span>UI Fitures</span>
              <span class="menu-arrow arrow_carrot-right"></span>
          </a>
          <ul class="sub">
              <li><a class="" href="general.html">Elements</a></li>
              <li><a class="" href="buttons.html">Buttons</a></li>
              <li><a class="" href="grids.html">Grids</a></li>
          </ul>
      </li>
      <li>
          <a class="" href="widgets.html">
              <i class="icon_genius"></i>
              <span>Widgets</span>
          </a>
      </li>
      <li>                     
          <a class="" href="chart-chartjs.html">
              <i class="icon_piechart"></i>
              <span>Relatórios</span>
              
          </a>
                             
      </li>
                 
      <li class="sub-menu">
          <a href="javascript:;" class="">
              <i class="icon_table"></i>
              <span>Tables</span>
              <span class="menu-arrow arrow_carrot-right"></span>
          </a>
          <ul class="sub">
              <li><a class="" href="basic_table.html">Basic Table</a></li>
          </ul>
      </li>                                    

'''