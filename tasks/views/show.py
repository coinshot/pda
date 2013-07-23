from django.db.models import Q
from django.views.generic import DetailView

from lib.mixins.views import LoginRequiredMixin, OwnedAndTaggedMixin

from ..models import Task, TaskItem


class ShowTaskView(LoginRequiredMixin, OwnedAndTaggedMixin, DetailView):
  model = Task
  template_name = 'tasks/show.html'

  def get_context_data(self, **kwargs):
    context = super(ShowTaskView, self).get_context_data(**kwargs)
    if context['task'].id:
      context['task_items'] = self.get_task_items(context['task'].id)
    print "CONTEXT: ", context
    return context

  def get_task_items(self, task_id):
    print "TASK: ", task_id
    return TaskItem.objects.filter(task_id=task_id)
