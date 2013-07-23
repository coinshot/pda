from django.core.urlresolvers import reverse
from django.views.generic import CreateView

from lib.mixins.views import LoginRequiredMixin, OwnedAndTaggedMixin

from ..forms import TaskForm
from ..models import Task


class NewTaskView(LoginRequiredMixin, OwnedAndTaggedMixin, CreateView):
  form_class = TaskForm
  model = Task
  template_name = 'tasks/new.haml'
  success_url = "/tasks/%(id)s/"
