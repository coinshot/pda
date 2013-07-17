from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LoginRequiredMixin(object):
  '''
  Mixin for securing class-based views
  by including the @login_required method decorator by default.
  '''

  @method_decorator(login_required)
  def dispatch(self, *args, **kwargs):
    return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)