# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='technicaldocument',
            name='created',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='technicaldocument',
            name='updated',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='technicaldocument',
            name='widget',
            field=models.ForeignKey(to='demo_site.Widget', related_name='documents'),
        ),
    ]
