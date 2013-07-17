from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _


class Calendar(models.Model):
  name = models.CharField(max_length = 100)
  slug = models.CharField(max_length = 16)
  owner = models.ForeignKey(User)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  class Meta:
    db_table = u'calendars'
    verbose_name = _('calendar')
    verbose_name_plural = _('calendars')
    app_label = 'planner'