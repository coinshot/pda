from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView

# from tagger.lib.forms import SearchTagForm
from ..models.note import Note


class MainNotepadView(ListView):
  model = Note
  template_name = 'notepad/index.html'
  # form_class = SearchTagForm
