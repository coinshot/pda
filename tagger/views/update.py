from django.views.generic.edit import FormView

from ..lib.forms import UpdateTagForm


class UpdateTagView(FormView):
  template_name = 'tagger/update.haml'
  form_class = UpdateTagForm
