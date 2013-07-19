from django.db.models import Q
from django.views.generic import ListView

from lib.mixins.views import LoginRequiredMixin, OwnedAndTaggedMixin

from ..forms import SearchNoteForm
from ..models.note import Note


class MainNotepadView(LoginRequiredMixin, OwnedAndTaggedMixin, ListView):
  model = Note
  template_name = 'notepad/index.html'

  def get_queryset(self):
    try:
      keyword = self.request.GET.get('kw')
    except:
      keyword = False

    result = super(MainNotepadView, self).get_queryset()
    if keyword:
      result = result.filter(Q(name__icontains = keyword) | Q(note__icontains = keyword))

    return result