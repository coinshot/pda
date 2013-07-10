from django.core.urlresolvers import reverse
from django.test import TestCase

from tagger.views import *

# Tagger routes
# Main Tags Index (needs to contain tag and counts)
# New/Create Tag
# Edit/Updat tag
# Delete Tag (cascade to children)
# Find or create tag (for app calls)
class TaggerRoutesTest(TestCase):
  def test_index(self):
    r = self.client.get(reverse('tagger_main'))
    self.assertEqual(r.status_code, 200)
