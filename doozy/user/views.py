from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
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
