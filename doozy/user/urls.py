from django.urls import path
from . import views


app_name = 'user'

urlpatterns = [
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
]
