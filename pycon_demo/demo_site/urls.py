from django.conf.urls import patterns, include
from . import views

urlpatterns = patterns('',
                       (r"^widgets/(?P<category_slug>[a-z0-9\-]+)/$", views.WidgetCategoryView.as_view()),
                       (r"^widgets/(?P<category_slug>[a-z0-9\-]+)/(?P<widget_slug>[a-zA-Z0-9\-]+)/$", views.WidgetView.as_view())
)
