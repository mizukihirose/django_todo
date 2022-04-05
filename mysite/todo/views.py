from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Todo

# Create your views here.

def index(request):
  todos_list = Todo.objects.order_by('-pub_date')
  context = {'todos_list': todos_list}
  return render(request, 'todo/index.html', context)


def detail(request, todo_id):
  todo = get_object_or_404(Todo, pk=todo_id)
  return render(request, 'todo/detail.html', {'todo':todo})


def add_todo(request):
  return render(request, 'todo/add_todo.html')

def modify_db(request):
  todo = Todo.objects.create(todo_text=request.POST["text"], due_date=request.POST["due"], importance=request.POST["importance"])
  return HttpResponseRedirect(reverse('todo:index'))