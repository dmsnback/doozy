from django.contrib import admin
from django.contrib.auth import urls
from django.urls import include, path


urlpatterns = [
    path('', include('tasks.urls')),
    path('auth/', include(urls)),
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
]
