from django.contrib.contenttypes.models import ContentType
from django.db.models import Q

from tagger.models import Tag, TagItem

class TaggedFormMixin(object):
  '''
  Used with forms, this mixin ensures
  that record being worked on is owned by the current user.
  '''

  def clean_tags(self):
    tags = self.cleaned_data.get('tags')
    return tags

  def save(self):
    instance = super(TaggedFormMixin, self).save()
    tags = self.cleaned_data.get('tags')
    self.save_tags(instance, tags)

    # print "self object id: ", instance.id
    # print "tags:  ", tags
    return instance

  def save_tags(self, instance, tags):
    owner_id = instance.owner_id
    print "owner: ", owner_id
    tag_list = tags.split(',')
    tag_items = []

    for e in tag_list:
      e = e.strip()
      tag = Tag.objects.get_or_create(name=e, owner_id=owner_id)[0]
      content_type = ContentType.objects.get_for_model(instance)
      tag_item = TagItem.objects.get_or_create(tag_id=tag.id, owner_id=owner_id, content_type=content_type, object_id=instance.id)[0]
      tag_items.append(tag_item.id)

    self.remove_tags

    return True

  def remove_tags(self, current_tag_ids):
    #
    return True