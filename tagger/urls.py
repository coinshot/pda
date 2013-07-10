from django.conf.urls import patterns, include, url, static
from django.conf.urls.defaults import *

from tagger import views

urlpatterns = patterns('.tagger.views',
  url(r'^$', views.MainView.as_view(), name='tagger_main'),

)


# Tagger routes
# Main Tags Index (needs to contain tag and counts)
# New/Create Tag
# Edit/Updat tag
# Delete Tag (cascade to children)
# Find or create tag (for app calls)