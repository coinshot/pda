from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _


class Location(models.Model):
  name = models.CharField(max_length = 250)
  user = models.ForeignKey(User)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  class Meta:
    db_table = u'locations'
    verbose_name = _('location')
    verbose_name_plural = _('locations')
    app_label = 'planner'