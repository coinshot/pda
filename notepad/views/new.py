from django.views.generic import CreateView

from lib.mixins.views import LoginRequiredMixin, OwnedAndTaggedMixin

from ..forms import NoteForm
from ..models.note import Note


class NewNotepadView(LoginRequiredMixin, OwnedAndTaggedMixin, CreateView):
  form_class = NoteForm
  template_name = 'notepad/new.html'
  success_url = '/notepad'
