from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _

from polymorphic import PolymorphicModel

from notepad.models.notes import *

from tagger.models.tag import *


class TaskTag(Tag):
  note = models.ForeignKey(Note)
  class Meta:
    db_table = u'note_tags'
    verbose_name = _('note tag')
    verbose_name_plural = _('note tags')
    app_label = 'notepad'