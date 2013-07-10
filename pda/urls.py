from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from notepad import views
from planner import views
from tagger import views
from tasks import views

urlpatterns = patterns('',
  url(r'^$', TemplateView.as_view(template_name='home.html'), name='home_page'),
  # url(r'^notepad/', include('notepad.urls')),
  # url(r'^planner/', include('planner.urls')),
  url(r'^tagger/', include('tagger.urls')),
  # url(r'^tasks/', include('tasks.urls')),
)
