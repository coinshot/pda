from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView

from lib.mixins.views import LoginRequiredMixin, OwnedMixin

from ..models.note import Note


class ShowNotepadView(LoginRequiredMixin, OwnedMixin, DetailView):
  model = Note
  template_name = 'notepad/show.html'

