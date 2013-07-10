from django.core.urlresolvers import reverse
from django.test import TestCase

from tagger.views import *

class TaggerRoutesTest(TestCase):
  def test_index(self):
    r = self.client.get(reverse('tagger_main'))
    self.assertEqual(r.status_code, 200)

  def test_new(self):
    r = self.client.get(reverse('tagger_new'))
    self.assertEqual(r.status_code, 200)

    r = self.client.post(reverse('tagger_new'))
    self.assertEqual(r.status_code, 200)

  def test_update(self):
    r = self.client.get(reverse('tagger_update'))
    self.assertEqual(r.status_code, 200)

    r = self.client.post(reverse('tagger_update'))
    self.assertEqual(r.status_code, 200)

  def test_delete(self):
    r = self.client.get(reverse('tagger_delete'))
    self.assertEqual(r.status_code, 304)

    r = self.client.post(reverse('tagger_update'))
    self.assertEqual(r.status_code, 200)

  def test_search(self):
    r = self.client.get(reverse('tagger_search'))
    self.assertEqual(r.status_code, 200)