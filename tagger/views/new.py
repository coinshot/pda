from django.views.generic.edit import FormView

from ..lib.forms import NewTagForm


class NewTagView(FormView):
  template_name = 'tagger/new.haml'
  form_class = NewTagForm
