from django.contrib import messages
from django.views.generic import DeleteView

from lib.mixins.views import LoginRequiredMixin, OwnedAndTaggedMixin

from ..models import Task


class DeleteTaskView(LoginRequiredMixin, OwnedAndTaggedMixin, DeleteView):
  model = Task
  template_name = 'tasks/delete.html'

  def get_success_url(self):
    model = self.__class__.__name__.replace('Delete', '').replace('padView', '')
    messages.add_message(self.request, messages.INFO, ("%s has been deleted" % model) )
    return '/tasks'
