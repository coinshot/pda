from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from tagger.lib.forms import *


class MainView(TemplateView):
  template_name = 'tagger/index.html'


class NewView(FormView):
  template_name = 'tagger/new.html'
  form_class = NewForm


class UpdateView(FormView):
  template_name = 'tagger/update.html'
  form_class = UpdateForm


class DeleteView(TemplateView):
  template_name = 'tagger/delete.html'


class SearchView(TemplateView):
  template_name = 'tagger/search.html'

