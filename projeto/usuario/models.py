from django.db import models
from django.conf import settings

from django.contrib.auth.models import User

#importa a função que detecta sinais de 'save', enviados ao salvar um modelo
from django.db.models.signals import post_save

class Perfil(models.Model):

    #Fazendo o relacionamento entre o usuario Django e o Perfil
    #Docs: https://docs.djangoproject.com/en/1.8/topics/auth/customizing/
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)

    #Foto do Usuário
    foto = models.FileField(upload_to="usuarios", default="user-avat.png")

    @property
    def name(self):
        return u"%s %s" % (self.user.first_name, self.user.family_name)

    def __str__(self):
        return '%s - %s' % (self.user.username, self.user.email)

    #Cria o perfil do usuário se o Django User existir, mas o perfil Usuário não existir.
    def perfil_existe(pk):

        user = User.objects.get(pk=pk)
        try:
            # fails if it doesn't exist
            perfil = user.userprofile
        except e:
            perfil = Perfil(user=user)
            perfil.save()
        return

    #Funcao que cria o UsuarioEncontro toda vez que um usuario for criado pelo Django.contrib.auth
    def cria_perfil(sender, instance, created, **kwargs):
        if created:
            Perfil.objects.create(user=instance)

    #Configurando o signal que detecta quando um usuario é criado e executa a funcao acima (cria_usuario_encontro) para termos o "Perfil".
    #Docs: https://docs.djangoproject.com/en/1.4/topics/auth/#storing-additional-information-about-users
    post_save.connect(cria_perfil, sender=User)
