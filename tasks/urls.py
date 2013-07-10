from django.conf.urls import patterns, include, url, static
from django.conf.urls.defaults import *

from tasks import views

urlpatterns = patterns('.tasks.views',
  url(r'^$', views.MainView.as_view(), name='tasks_main'),
)