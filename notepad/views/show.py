from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import DetailView

from ..models.note import Note


class ShowNotepadView(DetailView):
  model = Note
  template_name = 'notepad/show.html'

  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
    return super(ShowNotepadView, self).dispatch(request, *args, **kwargs)
