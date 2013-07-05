from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _


class Reminder(models.Model):
  DURATION = (
    ('minutes', 'Minutes'),
    ('hours', 'Hours'),
    ('days', 'Days'),
    ('weeks', 'Weeks'),
  )
  user = models.ForeignKey(User)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  class Meta:
    db_table = u'reminders'
    verbose_name = _('reminder')
    verbose_name_plural = _('reminders')