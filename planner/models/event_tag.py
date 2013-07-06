from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _

from polymorphic import PolymorphicModel

from planner.models.event import *

from tagger.models.tag import *


class EventTag(Tag):
  event = models.ForeignKey(Event)
  class Meta:
    db_table = u'event_tags'
    verbose_name = _('event tag')
    verbose_name_plural = _('event tags')
    app_label = 'planner'