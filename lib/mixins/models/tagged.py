class TaggedMixin(object):
  '''
  Mixin to automatically create, if necessary, and set the tags submitted.
  '''

  def save():
    model = super(TaggedMixin, self).save()

    return model
