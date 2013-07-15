from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


urlpatterns = patterns('',
  url(r'^$', TemplateView.as_view(template_name='site/home.html'), name='home_page'),
  url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'site/login.html'}, name='user_login'),
  url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'site/logged_out.html'}, name='user_logout'),

  url(r'^notepad/', include('notepad.urls')),
  url(r'^planner/', include('planner.urls')),
  url(r'^tagger/', include('tagger.urls')),
  url(r'^tasks/', include('tasks.urls')),
)
