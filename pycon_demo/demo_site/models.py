from mezzanine.core.models import Displayable, Orderable
from mezzanine.core.fields import FileField
from mezzanine.pages.models import Page, RichText
from django.db import models


class WidgetCategory(Displayable):

    def get_absolute_url(self):
        return '/widgets/{}/'.format(self.slug)


class Widget(Displayable, RichText):

    category = models.ForeignKey(WidgetCategory)

    def get_absolute_url(self):
        return self.category.get_absolute_url() + self.slug


class TechnicalDocument(Orderable):

    title = models.CharField(max_length=120)
    document = FileField()
    widget = models.ForeignKey(Widget)

    def __str__(self):
        return self.title


class Employee(Page, RichText):

    # Employees name with be in the title field
    position = models.CharField(max_length=60)
    photo = FileField(blank=True)
