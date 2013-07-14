from django.conf.urls import patterns, include, url, static
from django.conf.urls import *

from views import *

urlpatterns = patterns('.planner.views',
  url(r'^$', MainPlannerView.as_view(), name='planner_main'),
  # url(r'^search/$', views.MainView.as_view(), name='tagger_search'),
  # url(r'^new/$', views.NewView.as_view(), name='tagger_new'),
  # url(r'^update/(?P<pk>\d+)$', views.UpdateView.as_view(), name='tagger_update'),
  # url(r'^delete/$', views.DeleteView.as_view(), name='tagger_delete'),
)
