from django.conf.urls import patterns, include, url, static
from django.conf.urls import *

from .views import *

urlpatterns = patterns('',
  url(r'^$', MainNotepadView.as_view(), name='notepad_main'),
  url(r'^(?P<pk>\d+)/$', ShowNotepadView.as_view(), name='notepad_show_id'),
  # TODO: Fix slug-based route (add slug field to table)
  # url(r'^(?P<slug>\w+)/$', ShowNotepadView.as_view(), name='notepad_show_slug'),
  url(r'^new/$', NewNotepadView.as_view(), name='notepad_new'),
  url(r'^edit/(?P<pk>\d+)$', EditNotepadView.as_view(), name='notepad_edit'),
  # url(r'^edit/(?P<slug>\w+)$', EditNotepadView.as_view(), name='notepad_edit'),
  url(r'^delete/(?P<pk>\d+)$', DeleteNotepadView.as_view(), name='notepad_delete'),
)
