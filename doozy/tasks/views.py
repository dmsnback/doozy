from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from tasks.forms import TaskForm
from tasks.models import Task


def index(request):
    template_name = 'tasks/index.html'
    tasks = Task.objects.values(
        'id', 'title', 'priority__title', 'author__username',
    ).filter(completed=False)
    context = {'tasks': tasks}
    return render(request, template_name, context)


@login_required
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


@login_required
def task_edit(request, pk):
    template_name = 'tasks/create_task.html'
    instance = get_object_or_404(Task, pk=pk, author=request.user)
    form = TaskForm(request.POST or None, instance=instance)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('tasks:index')
    return render(request, template_name, context)


@login_required
def task_delete(request, pk):
    template_name = 'tasks/create_task.html'
    instance = get_object_or_404(Task, pk=pk)
    form = TaskForm(instance=instance)
    context = {'form': form}
    if request.method == 'POST':
        instance.delete()
        return redirect('tasks:index')
    return render(request, template_name, context)


@login_required
def task_list(request):
    template_name = 'tasks/task_list.html'
    task_list = Task.objects.values(
        'id', 'title', 'priority__title', 'author__username'
    ).order_by('completed', '-created_at')
    context = {'task_list': task_list}
    return render(request, template_name, context)
