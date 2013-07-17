from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _

from tagger.models.tag import *
from task import Task


class TaskTag(models.Model):
  task = models.ForeignKey(Task)
  tag = models.ForeignKey(Tag)
  owner = models.ForeignKey(User)
  class Meta:
    db_table = u'task_tags'
    verbose_name = _('task tag')
    verbose_name_plural = _('task tags')
    app_label = 'tasks'