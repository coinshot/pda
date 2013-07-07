from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _

from tagger.models.tag import *
from notepad.models.notes import *


class NoteTag(models.Model):
  note = models.ForeignKey(Note)
  tag = models.ForeignKey(Tag)
  class Meta:
    db_table = u'note_tags'
    verbose_name = _('note tag')
    verbose_name_plural = _('note tags')
    app_label = 'notepad'