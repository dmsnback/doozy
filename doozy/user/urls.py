from django.urls import path
from . import views


app_name = 'user'

urlpatterns = [
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path(
        'profile/<str:username>/edit/',
        views.user_profile_edit,
        name='user_profile_edit'
    ),
    path(
        'profile/<str:username>/delete/',
        views.user_profile_delete,
        name='user_profile_delete'
    ),
]
