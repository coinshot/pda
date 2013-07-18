from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext, ugettext_lazy as _

from .tag import Tag


class TagItem(models.Model):
  tag = models.ForeignKey(Tag)
  owner = models.ForeignKey(User)
  content_type = models.ForeignKey(ContentType)
  object_id = models.PositiveIntegerField()
  content_object = generic.GenericForeignKey('content_type', 'object_id')
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  class Meta:
    db_table = u'tag_items'
    verbose_name = _('tag item')
    verbose_name_plural = _('tag items')
    app_label = 'tagger'