from django.test import TestCase
from django.utils import timezone

from .models import Todo

import datetime

# Create your tests here.

class TodoModelTests(TestCase):
  def test_was_published_recently_with_future_date(self):
    time = timezone.now() + datetime.timedelta(days=30)
    future_published_todo = Todo(pub_date=time)
    self.assertIs(future_published_todo.was_published_recently(), False)


  def test_was_published_recently_with_old_date(self):
    time = timezone.now() - datetime.timedelta(days=30)
    old_published_todo = Todo(pub_date=time)
    self.assertIs(old_published_todo.was_published_recently(), False)


  def test_was_published_recently_with_recent_date(self):
    time = timezone.now() - datetime.timedelta(days=3)
    recently_published_todo = Todo(pub_date=time)
    self.assertIs(recently_published_todo.was_published_recently(), True)