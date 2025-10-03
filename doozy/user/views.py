from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from tasks.models import User
from user.forms import CustomUserCreationForm


def user_profile(request, username):
    template_name = 'users/profile.html'
    user = get_object_or_404(User.objects.all(), username=username)
    context = {'user': user}
    return render(request, template_name, context)


@login_required
def user_profile_edit(request, username):
    template_name = 'users/profile_edit.html'
    user = get_object_or_404(User, username=username)
    form = CustomUserCreationForm(request.POST or None, instance=user)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('user:user_profile')
    return render(request, template_name, context)


@login_required
def user_profile_delete(request, username):
    if request.method == 'POST':
        user = get_object_or_404(User, username=username)
        logout(request)
        user.delete()
    return redirect('tasks:index')
