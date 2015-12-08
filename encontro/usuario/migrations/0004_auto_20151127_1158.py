# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_auto_20151126_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarioencontro',
            name='foto',
            field=models.FileField(upload_to='usuarios', default='user-avat.png'),
        ),
    ]
