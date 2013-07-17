from django.views.generic import DeleteView

from lib.mixins.views import LoginRequiredMixin, OwnedMixin

from ..models.note import Note


class DeleteNotepadView(LoginRequiredMixin, OwnedMixin, DeleteView):
  model = Note
  template_name = 'notepad/delete.html'
  success_url = '/notepad'
