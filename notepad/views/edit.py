from django.views.generic import UpdateView

from lib.mixins.views import LoginRequiredMixin, OwnedMixin

from ..forms import NoteForm
from ..models.note import Note


class EditNotepadView(LoginRequiredMixin, OwnedMixin, UpdateView):
  form_class = NoteForm
  model = Note
  template_name = 'notepad/edit.html'
  success_url = "/notepad/%(id)s/"
