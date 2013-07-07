from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _


class Task(models.Model):
  user = models.ForeignKey(User)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  class Meta:
    db_table = u'tasks'
    verbose_name = _('task')
    verbose_name_plural = _('tasks')
    app_label = 'tasks'