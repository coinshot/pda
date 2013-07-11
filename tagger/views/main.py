from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from tagger.lib.forms import SearchTagForm


class MainView(FormView):
  template_name = 'tagger/index.html'
  form_class = SearchTagForm
