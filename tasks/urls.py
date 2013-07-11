from django.conf.urls import patterns, include, url, static
from django.conf.urls.defaults import *

from tasks import views


urlpatterns = patterns('.tasks.views',
  url(r'^$', views.MainView.as_view(), name='tasks_main'),
  url(r'^search/$', views.MainView.as_view(), name='tasks_search'),
  url(r'^new/$', views.NewView.as_view(), name='tasks_new'),
  url(r'^show/(?P<pk>\d+)$', views.ShowView.as_view(), name='tasks_show'),
  url(r'^update/(?P<pk>\d+)$', views.UpdateView.as_view(), name='tasks_update'),
  url(r'^delete/$', views.DeleteView.as_view(), name='tasks_delete'),
  # Task Items Routes
  url(r'^items/(?P<fk>\d+)$', views.ItemsView.as_view(), name='tasks_items'),
  url(r'^items/(?P<fk>\d+)/new/$', views.ItemNewView.as_view(), name='tasks_item_new'),
  url(r'^items/(?P<fk>\d+)/show/(?P<pk>\d+)$', views.ItemShowView.as_view(), name='tasks_item_show'),
  url(r'^items/(?P<fk>\d+)/update/(?P<pk>\d+)$', views.ItemUpdateView.as_view(), name='tasks_item_update'),
  url(r'^items/(?P<fk>\d+)/delete/$', views.ItemDeleteView.as_view(), name='tasks_item_delete'),
)
