from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView


class MainView(TemplateView):
  template_name = 'tasks/index.html'

class NewView(TemplateView):
  template_name = 'tasks/new.html'

class UpdateView(TemplateView):
  template_name = 'tasks/update.html'

class DeleteView(TemplateView):
  template_name = 'tasks/delete.html'

class SearchView(TemplateView):
  template_name = 'tasks/search.html'