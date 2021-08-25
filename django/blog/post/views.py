from django.http import HttpResponse


def index(request):
    key = request.GET.get("key")
    key = request.POST.get("key")
    return HttpResponse("Posts index view")
