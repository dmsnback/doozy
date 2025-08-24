from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib import admin
from django.contrib.auth import urls
from django.urls import include, path, reverse_lazy


urlpatterns = [
    path('', include('tasks.urls')),
    path('auth/', include(urls)),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('tasks:index'),
        ),
        name='registration',
        ),
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
]
