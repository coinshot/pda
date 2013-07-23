from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


urlpatterns = patterns('',
  url(r'^$', TemplateView.as_view(template_name='site/home.haml'), name='home_page'),
  url(r'^accounts/', include('accounts.urls')),
  url(r'^notepad/', include('notepad.urls')),
  url(r'^planner/', include('planner.urls')),
  url(r'^tagger/', include('tagger.urls')),
  url(r'^tasks/', include('tasks.urls')),
)
