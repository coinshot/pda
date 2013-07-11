from django.core.urlresolvers import reverse
from django.test import TestCase

from tagger.views import *


class TaggerRoutesTest(TestCase):
  def test_index(self):
    # GET
    r = self.client.get(reverse('tagger_main'))
    self.assertEqual(r.status_code, 200)
    # POST
    r = self.client.post(reverse('tagger_main'))
    self.assertEqual(r.status_code, 200)

  def test_search(self):
    # GET
    r = self.client.get(reverse('tagger_search'))
    self.assertEqual(r.status_code, 200)
    # POST
    r = self.client.post(reverse('tagger_search'))
    self.assertEqual(r.status_code, 200)

  def test_new(self):
    # GET
    r = self.client.get(reverse('tagger_new'))
    self.assertEqual(r.status_code, 200)
    # POST
    r = self.client.post(reverse('tagger_new'))
    self.assertEqual(r.status_code, 200)

  def test_update(self):
    # GET
    r = self.client.get(reverse('tagger_update'))
    self.assertEqual(r.status_code, 200)
    # POST
    r = self.client.post(reverse('tagger_update'))
    self.assertEqual(r.status_code, 200)

  def test_delete(self):
    # GET
    r = self.client.get(reverse('tagger_delete'), follow = True)
    self.assertEqual(r.status_code, 200)
    self.assertRedirects(r, reverse('tagger_main'))
    # POST
    r = self.client.post(reverse('tagger_update'))
    self.assertEqual(r.status_code, 200)