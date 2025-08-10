from django.shortcuts import render

from tasks.models import Task


def index(request):
    template_name = 'index.html'
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, template_name, context)
