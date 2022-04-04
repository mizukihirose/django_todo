from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Todo

# Create your views here.

def index(request):
  todos_list = Todo.objects.order_by('-pub_date')
  context = {'todos_list': todos_list}
  return render(request, 'todo/index.html', context)


def detail(request, todo_id):
  todo = get_object_or_404(Todo, pk=todo_id)
  return render(request, 'todo/detail.html', {'todo':todo})