class OwnedMixin(object):
  '''
  This mixin ensures that record/s being worked on is owned by the current user.
  '''

  def get_queryset(self):
    '''
    Filter queryset to records owned by the current user.
    '''
    result = super(OwnedMixin, self).get_queryset()
    result = result.filter(owner = self.request.user)
    return result

  def get_object(self, queryset = None):
    '''
    Restrict retrieval of an object if user does not own the record.
    '''
    obj = super(OwnedMixin, self).get_object()
    if obj.owner != self.request.user:
      raise Http404
    return obj

  def form_valid(self, form):
    '''
    Automatically insert user ownership to record before save().
    '''
    form.instance.owner_id = self.request.user.id
    return super(OwnedMixin, self).form_valid(form)