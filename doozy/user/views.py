from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from tasks.models import User
from user.forms import CustomUserCreationForm, CustomUserEditForm


class UserCreateView(CreateView):
        template_name = 'registration/registration_form.html'
        model = User
        form_class = CustomUserCreationForm
        success_url = '/'

        def form_valid(self, form):
            valid = super(UserCreateView, self).form_valid(form)
            new_user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )
            login(self.request, new_user)
            return valid


def user_profile(request, username):
    template_name = 'users/profile.html'
    user = get_object_or_404(User.objects.all(), username=username)
    context = {'user': user}
    return render(request, template_name, context)


@login_required
def user_profile_edit(request, username):
    template_name = 'users/profile_edit.html'
    user = get_object_or_404(User, username=username)
    if request.method == "POST":
        form = CustomUserEditForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
        return redirect('user:user_profile', username=user.username)
    else:
        form = CustomUserEditForm(instance=user)
    return render(request, template_name, {'form': form})


@login_required
def user_profile_delete(request, username):
    if request.method == 'POST':
        user = get_object_or_404(User, username=username)
        logout(request)
        user.delete()
    return redirect('tasks:index')


class CustomPasswordReset(PasswordResetView):
    template_name = "registration/password_reset_form.html"
    email_template_name = "registration/password_reset_email.html"
    subject_template_name = "registration/password_reset_subject.txt"
    success_url = reverse_lazy("passwort_reset_done_link")

    def form_valid(self, form):
        user_email = form.cleaned_data.get('email')
        response = super().form_valid(form)
        return redirect(f"{self.get_success_url()}?email={user_email}")


def passwort_reset_done_link(request):
    template_name = 'registration/password_reset_done.html'
    user_email = request.GET.get('email', '')
    email_domain = user_email.split('@')[-1]
    domain_map = {
        "yandex.ru": "https://mail.yandex.ru",
        "gmail.com": "https://mail.google.com",
        "mail.ru": "https://mail.ru",
        "bk.ru": "https://mail.ru",
        "inbox.ru": "https://mail.ru",
        "list.ru": "https://mail.ru",
    }
    mail_link = domain_map.get(email_domain, '#')
    context = {'mail_link': mail_link}
    return render(request, template_name, context)
