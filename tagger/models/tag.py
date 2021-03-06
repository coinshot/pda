from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _


class Tag(models.Model):
  name = models.SlugField()
  owner = models.ForeignKey(User)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  class Meta:
    db_table = u'tags'
    verbose_name = _('tag')
    verbose_name_plural = _('tags')
    app_label = 'tagger'