from django.conf.urls import patterns, include, url, static
# from django.conf.urls import *

from .views import *

urlpatterns = patterns('',
  url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, name='user_login'),
  url(r'^logout/$', logout_view, name='user_logout'),
  url(r'^signup/$', register_view, name='user_signup')
)