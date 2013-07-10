from django.conf.urls import patterns, include, url, static
from django.conf.urls.defaults import *

from tagger import views

urlpatterns = patterns('.tagger.views',
  url(r'^$', views.MainView.as_view(), name='tagger_main'),
  url(r'^new/$', views.NewView.as_view(), name='tagger_new'),
  url(r'^update/$', views.UpdateView.as_view(), name='tagger_update'),
  url(r'^delete/$', views.DeleteView.as_view(), name='tagger_delete'),
  url(r'^search/$', views.SearchView.as_view(), name='tagger_search'),
)


# Tagger routes
# Main Tags Index (needs to contain tag and counts)
# New/Create Tag
# Edit/Updat tag
# Delete Tag (cascade to children)
# Search Tag
