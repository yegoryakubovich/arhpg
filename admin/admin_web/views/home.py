from django.http import HttpResponseRedirect


def home_view(request):
    return HttpResponseRedirect("/")
