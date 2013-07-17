from django.views.generic import CreateView

from lib.mixins.views import LoginRequiredMixin, OwnedMixin

from ..forms import NoteForm
from ..models.note import Note


class NewNotepadView(LoginRequiredMixin, OwnedMixin, CreateView):
  form_class = NoteForm
  template_name = 'notepad/new.html'
  success_url = '/notepad'
