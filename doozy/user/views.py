from django.shortcuts import get_object_or_404, render
from tasks.models import User


def user_profile(request, username):
    template_name = 'users/profile.html'
    user = get_object_or_404(User.objects.all(), username=username)
    context = {'user': user}
    return render(request, template_name, context)
