from django.conf.urls import patterns, include, url, static
from django.conf.urls import *

from .views import *


urlpatterns = patterns('',
  url(r'^$', MainTaskView.as_view(), name='tasks_main'),
  url(r'^(?P<pk>\d+)/$', ShowTaskView.as_view(), name='tasks_show_id'),
  url(r'^new/$', NewTaskView.as_view(), name='tasks_new'),
  url(r'^edit/(?P<pk>\d+)$', EditTaskView.as_view(), name='tasks_edit'),
  url(r'^delete/(?P<pk>\d+)$', DeleteTaskView.as_view(), name='tasks_delete'),
  # # Task Items Routes
  # url(r'^items/(?P<fk>\d+)$', views.ItemsView.as_view(), name='tasks_items'),
  # url(r'^items/(?P<fk>\d+)/new/$', views.ItemNewView.as_view(), name='tasks_item_new'),
  # url(r'^items/(?P<fk>\d+)/show/(?P<pk>\d+)$', views.ItemShowView.as_view(), name='tasks_item_show'),
  # url(r'^items/(?P<fk>\d+)/update/(?P<pk>\d+)$', views.ItemUpdateView.as_view(), name='tasks_item_update'),
  # url(r'^items/(?P<fk>\d+)/delete/$', views.ItemDeleteView.as_view(), name='tasks_item_delete'),
)
