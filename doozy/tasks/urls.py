from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('task/create/', views.task_create, name='create'),
    path('task/<int:pk>/edit/', views.task_edit, name='edit'),
    path('task/<int:pk>/delete/', views.task_delete, name='delete'),
    path(
        'task/<int:pk>/task_detail_delete/',
        views.task_detail_delete,
        name='task_detail_delete'
    ),
    path('task/all/', views.task_list, name='task_list'),
    path('task/<int:pk>/', views.toggle_task, name='toggle_task'),
    path('task/<int:pk>/detail/', views.task_detail, name='task_detail'),

]
