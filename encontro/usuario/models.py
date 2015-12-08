from django.db import models
from django.conf import settings

#importamos o modelo de usuario do Django para "extende-lo"
from django.contrib.auth.models import User

#importa a função que detecta sinais de 'save', enviados ao salvar um modelo
from django.db.models.signals import post_save

class UsuarioEncontro(models.Model):

    #Fazendo o relacionamento entre o usuario Django e o player
    #Docs: https://docs.djangoproject.com/en/1.8/topics/auth/customizing/    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
    
    #Foto do Usuário
    foto = models.FileField(upload_to="usuarios", default="user-avat.png")

    @property
    def name(self):
        return u"%s %s" % (self.user.first_name, self.user.family_name)

    def __str__(self):
        return '%s - %s' % (self.user.username, self.user.email)
        
    #Cria o perfil do usuário (Usuario) se o Django User existir, mas o perfil Usuário não existir.
    def usuario_encontro_existe(pk):

        user = User.objects.get(pk=pk)
        try:
            # fails if it doesn't exist
            usuario_encontro = user.userprofile
        except e:
            usuario_encontro = UsuarioEncontro(user=user)
            usuario_encontro.save()
        return

    #Funcao que cria o UsuarioEncontro toda vez que um usuario for criado pelo Django.contrib.auth
    def cria_usuario_encontro(sender, instance, created, **kwargs):
        if created:
            UsuarioEncontro.objects.create(user=instance)

    #Configurando o signal que detecta quando um usuario é criado e executa a funcao acima (cria_usuario_encontro) para termos o "UsuarioEncontro".
    #Docs: https://docs.djangoproject.com/en/1.4/topics/auth/#storing-additional-information-about-users
    post_save.connect(cria_usuario_encontro, sender=User)


#class Person(models.Model):
#    first_name = models.CharField(max_length=200)
#    family_name = models.CharField(max_length=200)
#
#    @property
#    def name(self):
#        return u"%s %s" % (self.first_name, self.family_name)
#
#class PersonTable(tables.Table):
#    name = tables.Column(order_by=("first_name", "family_name"))