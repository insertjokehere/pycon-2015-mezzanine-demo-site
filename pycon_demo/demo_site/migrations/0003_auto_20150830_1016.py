# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('demo_site', '0002_auto_20150830_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='technicaldocument',
            name='_meta_title',
            field=models.CharField(max_length=500, blank=True, null=True, verbose_name='Title', help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.'),
        ),
        migrations.AddField(
            model_name='technicaldocument',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='technicaldocument',
            name='expiry_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Expires on', help_text="With Published chosen, won't be shown after this time"),
        ),
        migrations.AddField(
            model_name='technicaldocument',
            name='gen_description',
            field=models.BooleanField(default=True, verbose_name='Generate description', help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.'),
        ),
        migrations.AddField(
            model_name='technicaldocument',
            name='in_sitemap',
            field=models.BooleanField(default=True, verbose_name='Show in sitemap'),
        ),
        migrations.AddField(
            model_name='technicaldocument',
            name='keywords_string',
            field=models.CharField(blank=True, editable=False, max_length=500),
        ),
        migrations.AddField(
            model_name='technicaldocument',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Published from', help_text="With Published chosen, won't be shown until this time", db_index=True),
        ),
        migrations.AddField(
            model_name='technicaldocument',
            name='short_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='technicaldocument',
            name='site',
            field=models.ForeignKey(to='sites.Site', default=None, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technicaldocument',
            name='slug',
            field=models.CharField(max_length=2000, blank=True, null=True, verbose_name='URL', help_text='Leave blank to have the URL auto-generated from the title.'),
        ),
        migrations.AddField(
            model_name='technicaldocument',
            name='status',
            field=models.IntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2, verbose_name='Status', help_text='With Draft chosen, will only be shown for admin users on the site.'),
        ),
        migrations.AlterField(
            model_name='technicaldocument',
            name='title',
            field=models.CharField(verbose_name='Title', max_length=500),
        ),
    ]
