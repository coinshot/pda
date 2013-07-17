from django.views.generic import UpdateView

from lib.mixins.views import LoginRequiredMixin, OwnedMixin

from ..forms import NoteForm
from ..models.note import Note


class EditNotepadView(LoginRequiredMixin, OwnedMixin, UpdateView):
  form_class = NoteForm
  model = Note
  template_name = 'notepad/edit.html'
  success_url = "/notepad/%(id)s/"

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(EditNotepadView, self).form_valid(form)

  def get_object(self, queryset = None):
    obj = super(EditNotepadView, self).get_object()
    if obj.user_id != self.request.user.id:
      raise Http404
    return obj