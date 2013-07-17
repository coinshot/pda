from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import DeleteView

from lib.mixins.views import LoginRequiredMixin, OwnedMixin

from ..models.note import Note


class ShowNotepadView(LoginRequiredMixin, OwnedMixin, DeleteView):
  model = Note
  template_name = 'notepad/show.html'

