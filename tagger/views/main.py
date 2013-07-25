from django.views.generic.edit import FormView

from ..lib.forms import SearchTagForm


class MainTagView(FormView):
  template_name = 'tagger/index.haml'
  form_class = SearchTagForm
