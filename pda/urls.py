from django.conf.urls import patterns, include, url

from notes import views
from planner import views
from tagger import views
from tasks import views

urlpatterns = patterns('',
  url(r'^$', direct_to_template, {'templates':'home.html'}),
  url(r'^notepad/', include('notepad.urls')),
  url(r'^planner/', include('planner.urls')),
  url(r'^tagger/', include('tagger.urls')),
  url(r'^tasks/', include('tasks.urls')),
)
