from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, DeleteView
from django.views.generic.edit import FormView

from forms import UpdateTaskForm
from forms import SearchTaskForm

from models import Task


class MainTaskView(FormView):
  form_class = SearchTaskForm
  template_name = 'tasks/index.html'

class ShowTaskView(DetailView):
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