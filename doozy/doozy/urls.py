from django.contrib import admin
from django.contrib.auth import urls
from django.urls import include, path

from user.views import (
    CustomPasswordReset,
    UserCreateView, 
    passwort_reset_done_link
)


urlpatterns = [
    path('', include('tasks.urls')),
    path('auth/', include(urls)),
    path('registration/', UserCreateView.as_view(), name='register'),
    path(
        'password_reset/',
        CustomPasswordReset.as_view(),
        name='password_reset'
    ),
    path(
        'password_reset/done/',
        passwort_reset_done_link,
        name='passwort_reset_done_link'
    ),
    path('pages/', include('pages.urls')),
    path('user/', include('user.urls')),
    path('admin/', admin.site.urls),
]

handler404 = 'core.views.page_not_found'
handler500 = 'core.views.custom_500'
