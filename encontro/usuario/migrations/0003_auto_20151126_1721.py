# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20151101_1731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuarioencontro',
            old_name='usuario_django',
            new_name='user',
        ),
    ]
