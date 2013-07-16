from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView

from ..forms import NewNoteForm
from ..models.note import Note


class NewNotepadView(CreateView):
  form_class = NewNoteForm
  template_name = 'notepad/new.html'
  success_url = '/notepad'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(NewNotepadView, self).form_valid(form)
