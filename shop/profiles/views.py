import os

from django.shortcuts import render
import logging
from django.http import HttpResponse

from django.conf import settings

logger = logging.getLogger(__name__)


def profiles(request):
    if request.GET.get('param'):
        logger.info(f'My param: {request.GET.get("param")}')
    if request.GET:
        for key, value in request.GET.items():
            logger.info(f'My param: {key} - {value}')
    logger.info(os.getenv("MY_DEBUG_VARIABLE"))
    logger.info(type(os.getenv("MY_DEBUG_VARIABLE")))
    logger.info(settings.DEBUG)
    logger.info(type(settings.DEBUG))
    logger.info(settings.PRIMARY_VALUE)
    if settings.PRIMARY_VALUE == 'FUN':
        ERL = settings.FIRST_CHARACTER
        logger.info(f'Your character is {settings.FIRST_CHARACTER}')
    elif settings.PRIMARY_VALUE == 'SMART':
        ERL = settings.SECOND_CHARACTER
        logger.info(f'Your character is {settings.SECOND_CHARACTER}')
    else:
        ERL = 'LOSER'
        logger.info(f'Your character is LOSER')
    return HttpResponse(f"Profile index view. Hi, {ERL}")

