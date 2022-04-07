from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('<int:pk>/', views.DetailView.as_view(), name='detail'),
  path('add/', views.add_todo, name='add'),
  path('modify_db/', views.modify_db, name='modify_db')
]