from django.conf.urls import patterns, include, url, static
from django.conf.urls.defaults import *

from tagger import views

urlpatterns = patterns('.tagger.views',
  url(r'^$', views.MainView.as_view(), name='tagger_main'),
  url(r'^search/$', views.MainView.as_view(), name='tagger_search'),
  url(r'^new/$', views.NewView.as_view(), name='tagger_new'),
  url(r'^update/$', views.UpdateView.as_view(), name='tagger_update'),
  url(r'^delete/$', views.DeleteView.as_view(), name='tagger_delete'),
)
