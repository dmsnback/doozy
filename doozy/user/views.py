from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from tasks.models import User


def user_profile(request, username):
    template_name = 'users/profile.html'
    user = get_object_or_404(User.objects.all(), username=username)
    context = {'user': user}
    return render(request, template_name, context)


@login_required
def user_profile_edit(request, username):
    pass


@login_required
def user_profile_delete(request):
    if request.method == 'POST':
        user = get_object_or_404(User, username=request.user)
        logout(request)
        user.delete()
    return redirect('tasks:index')
