from django.views.generic.base import TemplateView
from . import models


class WidgetCategoryView(TemplateView):

    template_name = "widget/category.html"

    def get_context_data(self, **kwargs):
        context = super(WidgetCategoryView, self).get_context_data(**kwargs)
        context['category'] = models.WidgetCategory.objects.get(slug=kwargs['category_slug'])
        context['widgets'] = models.Widget.objects.filter(category=context['category'])
        return context


class WidgetView(TemplateView):

    template_name = "widget.html"

    def get_context_data(self, **kwargs):
        context = super(WidgetView, self).get_context_data(**kwargs)
        context['category'] = models.WidgetCategory.objects.published(for_user=self.request.user)\
                                                           .get(slug=kwargs['category_slug'])
        context['widget'] = context['category'].widget_set.published(for_user=self.request.user)\
                                                          .get(slug=kwargs['widget_slug'])
        return context
