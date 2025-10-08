from django.shortcuts import render


def page_not_found(request, exception):
    template_name = 'core/404.html'
    return render(request, template_name, status=404)


def csrf_failure(request, reason=''):
    template_name = 'core/403csrf.html'
    return render(request, template_name, status=403)


def custom_500(request):
    template_name = 'core/500.html'
    return render(request, template_name, status=500)
