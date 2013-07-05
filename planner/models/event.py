from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _


class Event(models.Model):
  name = models.CharField(max_length = 250)
  description = models.TextField()
  user = models.ForeignKey(User)
  start_at = models.DateTimeField()
  end_at = models.DateTimeField()
  whole_day = models.BooleanField()
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  class Meta:
    db_table = u'events'
    verbose_name = _('event')
    verbose_name_plural = _('events')