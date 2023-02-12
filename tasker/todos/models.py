from django.db import models

class TodoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class TodoItem(models.Model):
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    complete = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.text} | {"not " if not self.complete else ""}complete'
