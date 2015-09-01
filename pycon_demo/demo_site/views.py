from django.views.generic.base import TemplateView
from mezzanine.pages.page_processors import processor_for
from . import models


class WidgetCategoryView(TemplateView):

    template_name = "widget/category.html"

    def get_context_data(self, **kwargs):
        context = super(WidgetCategoryView, self).get_context_data(**kwargs)
        context['category'] = models.WidgetCategory.objects.get(slug=kwargs['category_slug'])
        context['widgets'] = models.Widget.objects.published(for_user=self.request.user)\
                                                  .filter(category=context['category'])
        context['editable_obj'] = context['category']
        return context


class WidgetView(TemplateView):

    template_name = "widget.html"

    def get_context_data(self, **kwargs):
        context = super(WidgetView, self).get_context_data(**kwargs)
        context['category'] = models.WidgetCategory.objects.published(for_user=self.request.user)\
                                                           .get(slug=kwargs['category_slug'])
        context['widget'] = context['category'].widget_set.published(for_user=self.request.user)\
                                                          .get(slug=kwargs['widget_slug'])

        context['documents'] = context['widget'].documents.published(for_user=self.request.user)
        context['editable_obj'] = context['widget']
        return context


@processor_for('widgets')
def widgets_index(request, page):
    if request.method == 'GET':
        return {
            'widgets': models.Widget.objects.published(for_user=request.user)
        }
    else:
        return {}
