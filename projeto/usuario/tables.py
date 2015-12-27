import django_tables2 as tables

from django.utils.safestring import mark_safe
from django.utils.html import escape
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User, Group

######################################################################################################################################################################
# Usuários ###########################################################################################################################################################
######################################################################################################################################################################

class ControlUsuarioColumn(tables.Column):
	def render(self, value):

		href_editar = reverse('editar_usuario', args=[str(value)])
		href_excluir = "new MyQuestion('Deseja realmente excluir esse registro?', '{}').question()".format(reverse('excluir_usuario', args=[str(value)]))
		href_senha = reverse('resetar_senha', args=[str(value)])

		return mark_safe('<a href="%s">Editar</a> | <a href="javascript:func()" onclick="%s">Excluir</a> | <a href="%s">Resetar Senha</a>' % (escape(href_editar), escape(href_excluir), escape(href_senha)))

class UsuarioTable(tables.Table):
	id = ControlUsuarioColumn(verbose_name=" ", attrs={"th": {"style": "width: 14%;"}})
	first_name = tables.Column(verbose_name="Nome")
	last_name = tables.Column(verbose_name="Sobrenome")
	email = tables.Column(verbose_name="Email")
	groups = tables.TemplateColumn("{{record.groups.all.0}}", verbose_name="Grupo")
	
	class Meta:
		model = User
		attrs = {"id": "tb_usuarios", "class": "table table-striped table-advance table-hover"}
		fields = ("first_name", "last_name", "email", "groups", "id")

######################################################################################################################################################################
# Grupos #############################################################################################################################################################
######################################################################################################################################################################

class ControlGroupColumn(tables.Column):
	def render(self, value):

		href_editar = reverse('editar_grupos', args=[str(value)])
		href_excluir = "new MyQuestion('Deseja realmente excluir esse registro?', '{}').question()".format(reverse('excluir_grupos', args=[str(value)]))

		return mark_safe('<a href="%s">Editar</a> | <a href="javascript:func()" onclick="%s">Excluir</a>' % (escape(href_editar), escape(href_excluir)))

class GroupTable(tables.Table):
	id = ControlGroupColumn(verbose_name=" ", attrs={"th": {"style": "width: 8%;"}})
	name = tables.Column(verbose_name="Nome")

	class Meta:
		model = Group
		attrs = {"id": "tb_grupos", "class": "table table-striped table-advance table-hover"}
		fields = ("name", "id")


#Para atributos em colunas
#>>> import django_tables2 as tables
#>>>
#>>> class SimpleTable(tables.Table):
#...     name = tables.Column(attrs={"th": {"id": "foo"}})
#...
#>>> SimpleTable(data).as_html()
#"{snip}<thead><tr><th id="foo" class="name">{snip}<tbody><tr><td class="name">{snip}"

# models.py
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

#Para não ordenar pela coluna
#id = tables.Column(verbose_name="Id", orderable=False)

#Para mudar a ordem de exibição das colunas
#sequence = ("name", "id")

#Para configurar os atributos das colunas
#name = tables.Column(attrs={"th": {"id": "foo"}})

#Tipos de colunas
#BooleanColumn – renders boolean values
#Column – generic column
#CheckBoxColumn – renders checkbox form inputs
#DateColumn – date formatting
#DateTimeColumn – datetime formatting in the local timezone
#FileColumn – renders files as links3
#EmailColumn – renders <a href="mailto:..."> tags
#LinkColumn – renders <a href="..."> tags (compose a django url)
#TemplateColumn – renders template code
#URLColumn – renders <a href="..."> tags (absolute url)

#>>> import django_tables2 as tables
#>>> import itertools
#>>> class SimpleTable(tables.Table):
#...     row_number = tables.Column(empty_values=())
#...     id = tables.Column()
#...     age = tables.Column()
#...
#...     def __init__(self, *args, **kwargs):
#...         super(SimpleTable, self).__init__(*args, **kwargs)
#...         self.counter = itertools.count()
#...
#...     def render_row_number(self):
#...         return 'Row %d' % next(self.counter)
#...
#...     def render_id(self, value):
#...         return '<%s>' % value
#...
#>>> table = SimpleTable([{'age': 31, 'id': 10}, {'age': 34, 'id': 11}])
#>>> for cell in table.rows[0]:
#...     print cell
#...
#Row 0
#<10>
#31

#>>> import django_tables2 as tables
#>>>
#>>> class UpperColumn(tables.Column):
#...     def render(self, value):
#...         return value.upper()
#...
#>>> class Example(tables.Table):
#...     normal = tables.Column()
#...     upper = UpperColumn()
#...
#>>> data = [{'normal': 'Hi there!',
#...          'upper':  'Hi there!'}]
#...
#>>> table = Example(data)
#>>> table.as_html()
#u'<table><thead><tr><th>Normal</th><th>Upper</th></tr></thead><tbody><tr><td>Hi there!</td><td>HI THERE!</td></tr></tbody></table>\n'
#
#>>> from django.utils.safestring import mark_safe
#>>> from django.utils.html import escape
#>>>
#>>> class ImageColumn(tables.Column):
#...     def render(self, value):
#...         return mark_safe('<img src="/media/img/%s.jpg" />'
#...                          % escape(value))
#...
