from django.contrib import admin
from mezzanine.core.admin import DisplayableAdmin, TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from . import models
import copy


class TechnicalDocumentInline(TabularDynamicInlineAdmin):
    model = models.TechnicalDocument

widget_fieldsets = copy.deepcopy(DisplayableAdmin.fieldsets)
widget_fieldsets[0][1]["fields"].insert(1, "category")
widget_fieldsets[0][1]["fields"].insert(1, "content")


class WidgetAdmin(DisplayableAdmin):

    fieldsets = widget_fieldsets
    inlines = (TechnicalDocumentInline,)

admin.site.register(models.Widget, WidgetAdmin)
admin.site.register(models.WidgetCategory, DisplayableAdmin)

admin.site.register(models.Employee, PageAdmin)
