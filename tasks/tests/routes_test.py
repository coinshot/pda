import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

from tasks.views import *
from tasks.models import Task


class TasksRoutesTest(TestCase):
  def create_user(self):
    u = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    u.save()
    return u

  def create_task(self):
    u = self.create_user()
    t = Task()
    t.user_id = u.id
    t.name = 'something'
    t.update_at = datetime.datetime.now()
    t.create_at = datetime.datetime.now()
    t.save()
    print t.id
    print u.id
    return t

  def test_index(self):
    # GET
    r = self.client.get(reverse('tasks_main'))
    self.assertEqual(r.status_code, 200)
    # POST
    r = self.client.post(reverse('tasks_main'))
    self.assertEqual(r.status_code, 200)

#   def test_search(self):
#     # GET
#     r = self.client.get(reverse('tagger_search'))
#     self.assertEqual(r.status_code, 200)
#     # POST
#     r = self.client.post(reverse('tagger_search'))
#     self.assertEqual(r.status_code, 200)

#   def test_show(self):
#     t = self.create_task()

#     # GET
#     r = self.client.get(reverse('tasks_show', kwargs = {'pk': t.id}))
#     self.assertEqual(r.status_code, 200)
#     # POST
#     r = self.client.post(reverse('tasks_show', kwargs = {'pk': t.id}), follow = True)
#     self.assertEqual(r.status_code, 200)
#     self.assertRedirects(r, reverse('tasks_main'))

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