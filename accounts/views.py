from django.contrib.auth import logout, authenticate, login
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import *


def logout_view(request):
  logout(request)
  is_logged_in = False
  return HttpResponseRedirect(reverse('home_page'))


def register_view(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      username = form.clean_username()
      password = form.clean_password2()
      form.save()
      user = authenticate(username = username, password = password)
      login(request, user)
      return HttpResponseRedirect(reverse('home_page'))
  else:
    form = UserRegistrationForm()

  return render(request, "accounts/register.haml", { 'form': form, })

def settings_view(request):
  return HttpResponseRedirect(reverse('home_page'))