from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from lib.mixins.views import LoginRequiredMixin, OwnedMixin

from ..forms import NoteForm
from ..models.note import Note


class NewNotepadView(LoginRequiredMixin, OwnedMixin, CreateView):
  form_class = NoteForm
  template_name = 'notepad/new.html'
  success_url = '/notepad'
