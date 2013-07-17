from django.db.models import Q
from django.views.generic import DetailView

from lib.mixins.views import LoginRequiredMixin, OwnedMixin

from ..models.note import Note


class ShowNotepadView(LoginRequiredMixin, OwnedMixin, DetailView):
  model = Note
  template_name = 'notepad/show.html'

