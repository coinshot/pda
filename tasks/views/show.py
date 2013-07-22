from django.db.models import Q
from django.views.generic import DetailView

from lib.mixins.views import LoginRequiredMixin, OwnedAndTaggedMixin

from ..models import Task


class ShowTaskView(LoginRequiredMixin, OwnedAndTaggedMixin, DetailView):
  model = Task
  template_name = 'tasks/show.html'

