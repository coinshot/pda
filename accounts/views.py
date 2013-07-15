from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from forms import


def logout_view(request):
  logout(request)
  is_logged_in = False
  return HttpResponseRedirect(reverse('home_page'))


def register_view(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      new_user = form.save()
      return HttpResponseRedirect(reverse('home_page'))
  else:
    form = UserRegistrationForm()

  return render(request, "accounts/register.html", { 'form': form, })