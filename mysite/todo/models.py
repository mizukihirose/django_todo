from pyexpat import model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Todo(models.Model):
  todo_text = models.CharField(max_length=200)
  is_done = models.BooleanField(default=False)
  pub_date = models.DateTimeField('date published')
  due_date = models.DateField('due date')
  importance = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])

  def __str__(self):
    return self.todo_text