
class OwnedMixin(object):

  def get_object(self, queryset = None):
    obj = super(OwnedMixin, self).get_object()
    if obj.user != self.request.user:
      raise Http404
    return obj

  def get_queryset(self):
    result = super(OwnedMixin, self).get_queryset()
    result = result.filter(user = self.request.user)
    return result

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(OwnedMixin, self).form_valid(form)