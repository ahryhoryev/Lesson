import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    get_first = request.GET.get("first")
    get_second = request.GET.get("second")
    email = request.POST.get("email")
    password = request.POST.get("password")
    logger.info(email)
    logger.info(password)
    return HttpResponse("Hello!")
