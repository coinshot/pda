from django.db import models
from django.contrib.auth.models import User
from planner.models.event import Event
from django.utils.translation import ugettext, ugettext_lazy as _


class Occurrence(models.Model):
  TIMEFRAMES = (
    ('DAILY', 'Daily'),
    ('WEEKLY', 'Weekly'),
    ('MONTHLY', 'Monthly'),
    ('YEARLY', 'Yearly'),
  )
  event = models.ForeignKey(Event)
  user = models.ForeignKey(User)
  repeat = models.PositiveSmallIntegerField()
  timeframe = models.CharField(max_length = 10, choices = TIMEFRAMES)
  start_at = models.DateField()
  end_at = models.DateField()
  ended = models.BooleanField()
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  class Meta:
    db_table = u'occurrences'
    verbose_name = _('occurrence')
    verbose_name_plural = _('occurrences')