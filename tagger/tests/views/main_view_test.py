from django.core.urlresolvers import reverse
from django.test import TestCase

from tagger.views import *


class MainViewTest(TestCase):
  def test_index(self):
    r = self.client.get(reverse('tagger_main'))
    self.assertEqual(r.status_code, 200)
    # self.assertContains(r, 'Home Library')