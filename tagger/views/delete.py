from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from tagger.lib.forms import *


class DeleteView(FormView):
  template_name = 'tagger/delete.html'
  form_class = UpdateTagForm

  def get(self, request, *args, **kwargs):
    return HttpResponseRedirect(reverse('tagger_main'))
