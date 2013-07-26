from django.contrib import messages
from django.contrib.contenttypes.models import ContentType

from lib.helpers import get_tag_slug

from tagger.models import Tag, TagItem


class OwnedAndTaggedMixin(object):
  '''
  This mixin ensures that record/s being worked on is owned by the current user.
  '''

  def form_valid(self, form):
    '''
    Automatically insert user relationship to record before save().
    '''
    form.instance.owner_id = self.request.user.id
    model = form.__class__.__name__.replace('Form', '')
    messages.add_message(self.request, messages.INFO, ("%s has been saved" % model) )
    return super(OwnedAndTaggedMixin, self).form_valid(form)

  # def get_success_url(self, form):
  #   success_url = super(OwnedAndTaggedMixin, self).get_absolute_url(self)
  #   # print form.get_absolute_url()
  #   return success_url

  def get_queryset(self):
    '''
    Filter queryset to records owned by the current user.
    '''
    result = super(OwnedAndTaggedMixin, self).get_queryset()
    result = result.filter(owner = self.request.user)
    return result

  def get_object(self):
    '''
    Restrict retrieval of an object if user does not own the record.
    '''
    obj = super(OwnedAndTaggedMixin, self).get_object()
    if obj.owner != self.request.user:
      raise Http404
    obj.tags = ["test_tag_one", "test_two"]
    obj.tags = self.get_tags()
    return obj

  def get_form_kwargs(self):
    '''
    Piggy-back request to initial value in kwargs
    '''
    kwargs = super(OwnedAndTaggedMixin, self).get_form_kwargs()
    kwargs['initial'] = {'owner':self.request.user}
    return kwargs

  def get_tags(self):
    '''
    Returns all record tags in a list.
    '''
    object_id = self.kwargs['pk']
    content_type = ContentType.objects.get_for_model(self.model)
    owner = self.request.user
    tags = Tag.objects.filter(owner_id=owner.id, tagitem__content_type_id=content_type.id, tagitem__object_id=object_id)
    tags_list = []
    if tags:
      tags_list = map(get_tag_slug, tags)
    return tags_list

