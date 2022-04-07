from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Todo

# Create your views here.

class IndexView(generic.ListView):
  template_name = 'todo/index.html'
  context_object_name = 'todo_list'

  def get_queryset(self):
      return Todo.objects.order_by('-pub_date')
      
# def index(request):
#   todos_list = Todo.objects.order_by('-pub_date')
#   context = {'todos_list': todos_list}
#   return render(request, 'todo/index.html', context)


class DetailView(generic.DetailView):
  model = Todo
  template_name = 'todo/detail.html'

# def detail(request, todo_id):
#   todo = get_object_or_404(Todo, pk=todo_id)
#   return render(request, 'todo/detail.html', {'todo':todo})


def add_todo(request):
  return render(request, 'todo/add_todo.html')

def modify_db(request):
  # due = request.POST["due"] if request.POST["due"] else None
  if request.POST["db_action"] == "add":
    if request.POST["due"]:
      Todo.objects.create(todo_text=request.POST["text"], due_date=request.POST["due"], importance=request.POST["importance"])
    else:
      Todo.objects.create(todo_text=request.POST["text"], importance=request.POST["importance"])
  elif request.POST["db_action"] == "delete":
    Todo.objects.filter(pk=request.POST["todo_id"]).delete()
  return HttpResponseRedirect(reverse('todo:index'))