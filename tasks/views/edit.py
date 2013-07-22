from django.views.generic import UpdateView

from lib.mixins.views import LoginRequiredMixin, OwnedAndTaggedMixin

from ..forms import TaskForm
from ..models import Task


class EditTaskView(LoginRequiredMixin, OwnedAndTaggedMixin, UpdateView):
  form_class = TaskForm
  model = Task
  template_name = 'tasks/edit.html'
  success_url = "/tasks/%(id)s/"
