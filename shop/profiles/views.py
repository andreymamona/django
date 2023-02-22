from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def profiles(request):
    logger.error(request.GET, request.POST)
    return HttpResponse("Profile index view")
