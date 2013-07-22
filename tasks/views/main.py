from django.db.models import Q
from django.views.generic import ListView

from lib.mixins.views import LoginRequiredMixin, OwnedAndTaggedMixin

# from ..forms import SearchTaskForm
from ..models import Task


class MainTaskView(LoginRequiredMixin, OwnedAndTaggedMixin, ListView):
  model = Task
  template_name = 'tasks/index.html'

  def get_queryset(self):
    try:
      keyword = self.request.GET.get('kw')
    except:
      keyword = False

    result = super(MainTaskView, self).get_queryset()
    if keyword:
      result = result.filter(Q(name__icontains = keyword) | Q(note__icontains = keyword))

    return result