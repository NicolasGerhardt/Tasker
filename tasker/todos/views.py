from django.http import HttpResponse
from django.shortcuts import render
from .models import TodoItem, TodoList

def index(req, id: int):
    todo_list = TodoList.objects.get(pk=id)
    item = todo_list.todoitem_set.get(pk=1)
    return HttpResponse('<h1>✨✨👾✨✨</h1><br/><h2>%s</h2>' % item.text)