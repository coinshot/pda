from django.conf.urls import patterns, include, url, static
from django.conf.urls import *

from .views import *


urlpatterns = patterns('',
  url(r'^$', MainTaskView.as_view(), name='tasks_main'),
  url(r'^(?P<pk>\d+)/$', ShowTaskView.as_view(), name='tasks_show_id'),
  url(r'^new/$', NewTaskView.as_view(), name='tasks_new'),
  url(r'^edit/(?P<pk>\d+)$', EditTaskView.as_view(), name='tasks_edit'),
  url(r'^delete/(?P<pk>\d+)$', DeleteTaskView.as_view(), name='tasks_delete'),

  # Task Items Routes
  # url(r'^(?P<fk>\d+)/show/(?P<pk>\d+)$', ShowItemView.as_view(), name='tasks_item_show'),
  url(r'^(?P<fk>\d+)/task_items/edit/(?P<pk>\d+)$', EditItemView.as_view(), name='tasks_item_edit'),
  # JSON Routes
  url(r'^task_item/new/$', create_task_item, name='task_item_new'),
  url(r'^task_item/delete/(?P<pk>\d+)$', delete_task_item, name='task_item_delete'),
  # url(r'^task_item/test/$', task_item_test, name='task_item_test'),
)

