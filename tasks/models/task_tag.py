from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _

from task import *
from tagger.models.tag import *


class TaskTag(models.Model):
  task = models.ForeignKey(Task)
  tag = models.ForeignKey(Tag)
  class Meta:
    db_table = u'task_tags'
    verbose_name = _('task tag')
    verbose_name_plural = _('task tags')
    app_label = 'tasks'