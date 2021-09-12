import random
import requests

from django.core.cache import cache

from rest_framework import status
from rest_framework.response import Response

TOKEN = '5A4A484458746E6777506473307136534D6F4C7851434C5577377637364332453056474C2B6F6C697167773D'
URL = 'https://api.kavenegar.com/v1/{token}/sms/send.json'.format(token=TOKEN)


def send_sms(value):
    message = 'باعرض سلام کد تایید شما {} میباشد.'.format(value)
    data = {
        'receptor': '09302658144',
        'message': message
    }
    requests.post(url=URL, data=data)


def code_generator():
    return random.randint(10000, 99999)


def handle_sms(request):
    code = code_generator()
    send_sms(code)
    cache.set('username', request.data.get('username', ''), timeout=90)
    cache.set('password', request.data.get('password', ''), timeout=90)
    cache.set('code', code, timeout=90)
    return Response({'message': 'successful'}, status=status.HTTP_200_OK)
