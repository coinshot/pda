from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _

from tagger.models.tag import *
from planner.models.event import *


class EventTag(models.Model):
  event = models.ForeignKey(Event)
  tag = models.ForeignKey(Tag)
  class Meta:
    db_table = u'event_tags'
    verbose_name = _('event tag')
    verbose_name_plural = _('event tags')
    app_label = 'planner'