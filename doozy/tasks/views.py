from django.shortcuts import get_object_or_404, redirect, render

from tasks.forms import TaskForm
from tasks.models import Task


def index(request):
    template_name = 'tasks/index.html'
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, template_name, context)


def task_create(request):
    template_name = 'tasks/create_task.html'
    form = TaskForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        return redirect('tasks:index')
    return render(request, template_name, context)


def task_edit(request, pk):
    template_name = 'tasks/create_task.html'
    instance = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=instance)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('tasks:index')
    return render(request, template_name, context)


def task_delete(request, pk):
    template_name = 'tasks/create_task.html'
    instance = get_object_or_404(Task, pk=pk)
    form = TaskForm(instance=instance)
    context = {'form': form}
    if request.method == 'POST':
        instance.delete()
        return redirect('tasks:index')
    return render(request, template_name, context)
