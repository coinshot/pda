from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from ..forms import NoteForm
from ..models.note import Note


class EditNotepadView(UpdateView):
  form_class = NoteForm
  model = Note
  template_name = 'notepad/edit.html'
  success_url = "/notepad/%(id)s/"

  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
    return super(EditNotepadView, self).dispatch(request, *args, **kwargs)

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(EditNotepadView, self).form_valid(form)

  # def get_success_url(self):
  #   return reverse('notepad_show')