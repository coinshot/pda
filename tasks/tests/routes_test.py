from django.core.urlresolvers import reverse
from django.test import TestCase

from tasks.views import *
from tasks.models import Task


class TasksRoutesTest(TestCase):
  def test_index(self):
    # GET
    r = self.client.get(reverse('tasks_main'))
    self.assertEqual(r.status_code, 200)
    # POST
    r = self.client.post(reverse('tasks_main'))
    self.assertEqual(r.status_code, 200)

  def test_search(self):
    # GET
    r = self.client.get(reverse('tagger_search'))
    self.assertEqual(r.status_code, 200)
    # POST
    r = self.client.post(reverse('tagger_search'))
    self.assertEqual(r.status_code, 200)

  def test_show(self):
    # GET
    r = self.client.get(reverse('tasks_show', kwargs = {'pk': 1}))
    self.assertEqual(r.status_code, 200)
    # POST
    r = self.client.post(reverse('tasks_show', kwargs = {'pk': 1}), follow = True)
    self.assertEqual(r.status_code, 200)
    self.assertRedirects(r, reverse('tasks_main'))

  # def test_new(self):
  #   # GET
  #   r = self.client.get(reverse('tasks_new'))
  #   self.assertEqual(r.status_code, 200)
  #   # POST
  #   r = self.client.post(reverse('tasks_new'))
  #   self.assertEqual(r.status_code, 200)

  # def test_update(self):
  #   # GET
  #   r = self.client.get(reverse('tasks_update'))
  #   self.assertEqual(r.status_code, 200)
  #   # POST
  #   r = self.client.post(reverse('tasks_update'))
  #   self.assertEqual(r.status_code, 200)

  # def test_delete(self):
  #   # GET
  #   r = self.client.get(reverse('tasks_delete'))
  #   self.assertEqual(r.status_code, 302)
  #   # POST
  #   r = self.client.post(reverse('tasks_update'))
  #   self.assertEqual(r.status_code, 200)


# class TaskItemsTest(TestCase):
#   def test_index(self):
#     # GET
#     r = self.client.get(reverse('tasks_items'))
#     self.assertEqual(r.status_code, 200)

#   def test_view(self):
#     # GET
#     r = self.client.get(reverse('tasks_item_show'))
#     self.assertEqual(r.status_code, 200)

#     # POST
#     r = self.client.post(reverse('tasks_item_show'), follow = True)
#     self.assertEqual(r.status_code, 200)
#     self.assertRedirects(r, reverse('tasks_main'))

#   def test_new(self):
#     # GET
#     r = self.client.get(reverse('tasks_item_new'))
#     self.assertEqual(r.status_code, 200)
#     # POST
#     r = self.client.post(reverse('tasks_item_new'))
#     self.assertEqual(r.status_code, 200)

#   def test_update(self):
#     # GET
#     r = self.client.get(reverse('tasks_item_update'))
#     self.assertEqual(r.status_code, 200)
#     # POST
#     r = self.client.post(reverse('tasks_item_update'))
#     self.assertEqual(r.status_code, 200)

#   def test_delete(self):
#     # GET
#     r = self.client.get(reverse('tasks_item_delete'))
#     self.assertEqual(r.status_code, 200)
#     # POST
#     r = self.client.post(reverse('tasks_item_delete'), {'pk': 1})
#     self.assertEqual(r.status_code, 200)