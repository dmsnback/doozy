from django.shortcuts import render

from tasks.forms import TaskForm 
from tasks.models import Task


def index(request):
    template_name = 'index.html'
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, template_name, context)


def task_create(request):
    template_name = 'create_task.html'
    form = TaskForm()
    context = {'form': form}
    return render(request, template_name, context)
