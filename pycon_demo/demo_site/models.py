from mezzanine.core.models import Displayable
from mezzanine.core.fields import RichTextField
from django.db import models


class WidgetCategory(Displayable):

    def get_absolute_url(self):
        return '/widgets/{}/'.format(self.slug)


class Widget(Displayable):

    category = models.ForeignKey(WidgetCategory)
    content = RichTextField()

    def get_absolute_url(self):
        return self.category.get_absolute_url() + self.slug


class TechnicalDocument(models.Model):
