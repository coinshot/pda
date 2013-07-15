from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from ..forms import NewNoteForm
from ..models.note import Note


class NewNotepadView(FormView):
  template_name = 'notepad/new.html'
  form_class = NewNoteForm
