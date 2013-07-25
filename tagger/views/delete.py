from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView

from ..lib.forms import *


class DeleteTagView(FormView):
  template_name = 'tagger/delete.haml'
  form_class = UpdateTagForm

  def get(self, request, *args, **kwargs):
    return HttpResponseRedirect(reverse('tagger_main'))
