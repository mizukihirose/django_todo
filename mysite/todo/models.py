from pyexpat import model
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator

import datetime

# Create your models here.
class Todo(models.Model):
  todo_text = models.CharField(max_length=200, validators=[MinLengthValidator(1)])
  is_done = models.BooleanField(default=False)
  pub_date = models.DateTimeField('date published', default=datetime.datetime.now)
  due_date = models.DateField('due date', null=True)
  importance = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])


  def __str__(self):
    return self.todo_text
  

  def was_published_recently(self):
    return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=7)