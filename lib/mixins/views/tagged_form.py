from django.contrib.contenttypes.models import ContentType
from django.db.models import Q

from tagger.models import Tag, TagItem

class TaggedFormMixin(object):
  '''
  Used with forms, this mixin ensures
  that record being worked on is owned by the current user.
  '''

  def __init__(self, *args, **kwargs):
    instance = kwargs['instance']
    if instance:
      owner = kwargs['initial']['owner']
      tags = self.get_tags(owner, instance)
      initial = kwargs['initial']
      initial['tags'] = tags
      kwargs['initial'] = initial
    super(TaggedFormMixin, self).__init__(*args, **kwargs)

  def save(self):
    instance = super(TaggedFormMixin, self).save()
    tags = self.cleaned_data.get('tags')
    self.save_tags(instance, tags)
    return instance

  def save_tags(self, instance, tags):
    owner_id = instance.owner_id
    tag_list = tags.split(',')
    tag_items = []

    for e in tag_list:
      e = e.strip()
      content_type = ContentType.objects.get_for_model(instance)
      tag = Tag.objects.get_or_create(name=e, owner_id=owner_id)[0]
      tag_item = TagItem.objects.get_or_create(tag_id=tag.id, owner_id=owner_id, content_type=content_type, object_id=instance.id)[0]
      tag_items.append(tag_item.id)

    self.remove_tags(tag_items, owner_id, content_type, instance.id)
    return True

  def remove_tags(self, current_tag_ids, owner,content_type, object_id):
    tagged_all = TagItem.objects.filter(owner_id=owner, content_type=content_type, object_id=object_id)
    for e in tagged_all:
      if not e.id in current_tag_ids:
        # delete relationship. no need to delete the tag
        e.delete()
    return True

  def get_tags(self, owner, instance):
    content_type = ContentType.objects.get_for_model(instance)
    tags = Tag.objects.filter(tagitem__content_type_id=content_type.id, tagitem__object_id=instance.id)
    tags_str = ""
    if tags.count() > 0:
      tags_str = map(get_tag_slug, tags)
      tags_str = ", ".join(tags_str)
    return tags_str

def get_tag_slug(tag):
  return tag.name
