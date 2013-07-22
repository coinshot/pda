from django.contrib.contenttypes.models import ContentType

from tagger.models import Tag, TagItem

class TaggedFormMixin(object):
  '''
  This mixin ensures that record being worked on is owned by the current user.
  '''

  def __init__(self, *args, **kwargs):
    '''
    Inserts a record's tags into the tag field's initial value.
    '''
    instance = kwargs['instance']
    if instance:
      owner = kwargs['initial']['owner']
      tags = self.get_tags(owner, instance)
      initial = kwargs['initial']
      initial['tags'] = tags
      kwargs['initial'] = initial
    return super(TaggedFormMixin, self).__init__(*args, **kwargs)

  def save(self):
    '''
    Intercept save call to save the record's tags.
    '''
    instance = super(TaggedFormMixin, self).save()
    tags = self.cleaned_data.get('tags')
    self.save_tags(instance, tags)
    return instance

  def save_tags(self, instance, tags):
    '''
    Saves all comma-delimited keywords as tags.
    '''
    content_type = ContentType.objects.get_for_model(instance)
    owner_id = instance.owner_id
    tags = tags.strip()
    tag_items = []
    if len(tags) > 0:
      tag_list = tags.split(',')
      for e in tag_list:
        e = e.strip()
        tag = Tag.objects.get_or_create(name=e, owner_id=owner_id)[0]
        tag_item = TagItem.objects.get_or_create(tag_id=tag.id, owner_id=owner_id, content_type=content_type, object_id=instance.id)[0]
        tag_items.append(tag_item.id)
    self.remove_tags(tag_items, owner_id, content_type, instance.id)

  def remove_tags(self, current_tag_ids, owner,content_type, object_id):
    '''
    Compares current tag list to old list and removes stale relationships.
    '''
    tagged_all = TagItem.objects.filter(owner_id=owner, content_type=content_type, object_id=object_id)
    for e in tagged_all:
      if not e.id in current_tag_ids:
        # delete relationship. no need to delete the tag
        e.delete()

  def get_tags(self, owner, instance):
    '''
    Returns all record tags in a comma-delimited string.
    '''
    content_type = ContentType.objects.get_for_model(instance)
    tags = Tag.objects.filter(owner_id=owner.id, tagitem__content_type_id=content_type.id, tagitem__object_id=instance.id)
    tags_str = ""
    if tags.count() > 0:
      tags_str = map(get_tag_slug, tags)
      tags_str = ", ".join(tags_str)
    return tags_str


def get_tag_slug(tag):
  '''
  Used for map iteration to get the tag keyword/slug.
  '''
  return tag.name

