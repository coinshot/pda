from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from ..forms.search_note import SearchNoteForm
from ..models.note import Note


class MainNotepadView(ListView):
  model = Note
  template_name = 'notepad/index.html'

  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
    return super(MainNotepadView, self).dispatch(request, *args, **kwargs)

  def get_queryset(self):
    try:
      keyword = self.request.GET.get('kw')
    except:
      keyword = False

    result = super(MainNotepadView, self).get_queryset()
    result = result.filter(user = self.request.user)
    if keyword:
      result = result.filter(Q(name__icontains = keyword) | Q(note__icontains = keyword))

    return result