from django.conf.urls import patterns, include, url, static
from django.conf.urls import *

from notepad.views import *

urlpatterns = patterns('.planner.views',
  url(r'^$', MainNotepadView.as_view(), name='notepad_main'),
  # url(r'^search/$', MainNotepadView.as_view(), name='tagger_search'),
  url(r'^new/$', NewNotepadView.as_view(), name='notepad_new'),
  # url(r'^update/(?P<pk>\d+)$', UpdateNotepadView.as_view(), name='tagger_update'),
  # url(r'^delete/$', DeleteNotepadView.as_view(), name='tagger_delete'),
)
