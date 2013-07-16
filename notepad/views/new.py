from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from ..forms import NewNoteForm
from ..models.note import Note


class NewNotepadView(CreateView):
  form_class = NewNoteForm
  template_name = 'notepad/new.html'
  success_url = '/notepad'

  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
    return super(MainNotepadView, self).dispatch(request, *args, **kwargs)

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(NewNotepadView, self).form_valid(form)
