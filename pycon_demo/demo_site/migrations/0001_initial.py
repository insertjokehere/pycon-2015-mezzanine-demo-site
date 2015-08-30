# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('page_ptr', models.OneToOneField(to='pages.Page', serialize=False, primary_key=True, auto_created=True, parent_link=True)),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('position', models.CharField(max_length=60)),
                ('photo', mezzanine.core.fields.FileField(blank=True, max_length=255)),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='TechnicalDocument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('_order', mezzanine.core.fields.OrderField(verbose_name='Order', null=True)),
                ('title', models.CharField(max_length=120)),
                ('document', mezzanine.core.fields.FileField(max_length=255)),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('keywords_string', models.CharField(editable=False, blank=True, max_length=500)),
                ('title', models.CharField(verbose_name='Title', max_length=500)),
                ('slug', models.CharField(verbose_name='URL', max_length=2000, help_text='Leave blank to have the URL auto-generated from the title.', blank=True, null=True)),
                ('_meta_title', models.CharField(verbose_name='Title', max_length=500, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', blank=True, null=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('gen_description', models.BooleanField(verbose_name='Generate description', help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', default=True)),
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('status', models.IntegerField(verbose_name='Status', choices=[(1, 'Draft'), (2, 'Published')], help_text='With Draft chosen, will only be shown for admin users on the site.', default=2)),
                ('publish_date', models.DateTimeField(verbose_name='Published from', help_text="With Published chosen, won't be shown until this time", db_index=True, null=True, blank=True)),
                ('expiry_date', models.DateTimeField(verbose_name='Expires on', help_text="With Published chosen, won't be shown after this time", blank=True, null=True)),
                ('short_url', models.URLField(blank=True, null=True)),
                ('in_sitemap', models.BooleanField(verbose_name='Show in sitemap', default=True)),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WidgetCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('keywords_string', models.CharField(editable=False, blank=True, max_length=500)),
                ('title', models.CharField(verbose_name='Title', max_length=500)),
                ('slug', models.CharField(verbose_name='URL', max_length=2000, help_text='Leave blank to have the URL auto-generated from the title.', blank=True, null=True)),
                ('_meta_title', models.CharField(verbose_name='Title', max_length=500, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', blank=True, null=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('gen_description', models.BooleanField(verbose_name='Generate description', help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', default=True)),
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('status', models.IntegerField(verbose_name='Status', choices=[(1, 'Draft'), (2, 'Published')], help_text='With Draft chosen, will only be shown for admin users on the site.', default=2)),
                ('publish_date', models.DateTimeField(verbose_name='Published from', help_text="With Published chosen, won't be shown until this time", db_index=True, null=True, blank=True)),
                ('expiry_date', models.DateTimeField(verbose_name='Expires on', help_text="With Published chosen, won't be shown after this time", blank=True, null=True)),
                ('short_url', models.URLField(blank=True, null=True)),
                ('in_sitemap', models.BooleanField(verbose_name='Show in sitemap', default=True)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='widget',
            name='category',
            field=models.ForeignKey(to='demo_site.WidgetCategory'),
        ),
        migrations.AddField(
            model_name='widget',
            name='site',
            field=models.ForeignKey(editable=False, to='sites.Site'),
        ),
        migrations.AddField(
            model_name='technicaldocument',
            name='widget',
            field=models.ForeignKey(to='demo_site.Widget'),
        ),
    ]
