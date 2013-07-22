from django.db.models import Q
from django.views.generic import DetailView

from lib.mixins.views import LoginRequiredMixin, OwnedAndTaggedMixin

from ..models import Note


class ShowNotepadView(LoginRequiredMixin, OwnedAndTaggedMixin, DetailView):
  model = Note
  template_name = 'notepad/show.html'

