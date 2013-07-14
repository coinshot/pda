from django.conf.urls import patterns, include, url, static
from django.conf.urls import *

from views import *


urlpatterns = patterns('.tagger.views',
  url(r'^$', MainTagView.as_view(), name='tagger_main'),
  url(r'^search/$', MainTagView.as_view(), name='tagger_search'),
  url(r'^new/$', NewTagView.as_view(), name='tagger_new'),
  url(r'^update/(?P<pk>\d+)$', UpdateTagView.as_view(), name='tagger_update'),
  url(r'^delete/$', DeleteTagView.as_view(), name='tagger_delete'),
)
