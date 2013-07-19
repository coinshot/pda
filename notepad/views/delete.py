from django.views.generic import DeleteView

from lib.mixins.views import LoginRequiredMixin, OwnedAndTaggedMixin

from ..models.note import Note


class DeleteNotepadView(LoginRequiredMixin, OwnedAndTaggedMixin, DeleteView):
  model = Note
  template_name = 'notepad/delete.html'
  success_url = '/notepad'
