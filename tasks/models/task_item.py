from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _

from task import Task


class TaskItem(models.Model):
  name = models.CharField(max_length = 250)
  completed = models.BooleanField()
  task = models.ForeignKey(Task)
  user = models.ForeignKey(User)
  expected_at = models.DateTimeField(null = True)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  class Meta:
    db_table = u'task_items'
    verbose_name = _('task item')
    verbose_name_plural = _('task items')
    app_label = 'tasks'