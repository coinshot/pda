from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, DeleteView
from django.views.generic.edit import FormView

from tasks.lib.forms import UpdateTaskForm
from tasks.lib.forms import SearchTaskForm

from tasks.models import Task


class MainView(FormView):
  form_class = SearchTaskForm
  template_name = 'tasks/index.html'

class ShowView(DetailView):
  model = Task
  template_name = 'tasks/show.html'


# class NewView(TemplateView):
#   template_name = 'tasks/new.html'

# class UpdateView(TemplateView):
#   template_name = 'tasks/update.html'

# class DeleteView(TemplateView):
#   template_name = 'tasks/delete.html'

# class SearchView(TemplateView):
#   template_name = 'tasks/search.html'

# class ItemsView(TemplateView):
#   template_name = 'tasks/index.html'

# class ItemNewView(TemplateView):
#   template_name = 'tasks/index.html'

# class ItemShowView(TemplateView):
#   template_name = 'tasks/index.html'

# class ItemUpdateView(TemplateView):
#   template_name = 'tasks/index.html'

# class ItemDeleteView(FormView):
#   template_name = 'tasks/index.html'
#   form_class = UpdateTaskForm