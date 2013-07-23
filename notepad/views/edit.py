from django.views.generic import UpdateView

from lib.mixins.views import LoginRequiredMixin, OwnedAndTaggedMixin

from ..forms import NoteForm
from ..models import Note


class EditNotepadView(LoginRequiredMixin, OwnedAndTaggedMixin, UpdateView):
  form_class = NoteForm
  model = Note
  template_name = 'notepad/edit.haml'
  success_url = "/notepad/%(id)s/"
