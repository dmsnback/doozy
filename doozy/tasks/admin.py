from django.contrib import admin

from tasks.models import PriorityTask, Task


admin.site.register(Task)
admin.site.register(PriorityTask)
