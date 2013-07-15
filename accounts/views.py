from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def logout_view(request):
  logout(request)
  is_logged_in = False
  return HttpResponseRedirect(reverse('home_page'))