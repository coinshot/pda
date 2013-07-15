from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView


# from tagger.lib.forms import SearchTagForm
from ..models.note import Note


class MainNotepadView(ListView):
  model = Note
  template_name = 'notepad/index.html'
  # form_class = SearchTagForm

  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
      return super(MainNotepadView, self).dispatch(request, *args, **kwargs)