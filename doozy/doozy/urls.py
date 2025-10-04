from django.contrib import admin
from django.contrib.auth import urls
from django.urls import include, path

from user.views import UserCreateView


urlpatterns = [
    path('', include('tasks.urls')),
    path('auth/', include(urls)),
    path('registration/', UserCreateView.as_view(), name='register'),
    path('pages/', include('pages.urls')),
    path('user/', include('user.urls')),
    path('admin/', admin.site.urls),
]
