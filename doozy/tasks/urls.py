from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('task/create/', views.task_create, name='create'),
    path('task/<int:pk>/edit/', views.task_edit, name='edit'),
    path('task/<int:pk>/delete/', views.task_delete, name='delete'),
]
