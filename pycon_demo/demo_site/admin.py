from django.contrib import admin
from mezzanine.core.admin import DisplayableAdmin
from . import models
import copy


widget_fieldsets = copy.deepcopy(DisplayableAdmin.fieldsets)
widget_fieldsets[0][1]["fields"].insert(1, "category")
widget_fieldsets[0][1]["fields"].insert(1, "content")


class WidgetAdmin(DisplayableAdmin):

    fieldsets = widget_fieldsets

admin.site.register(models.Widget, WidgetAdmin)
admin.site.register(models.WidgetCategory, DisplayableAdmin)
