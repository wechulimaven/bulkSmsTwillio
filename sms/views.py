from django.shortcuts import render
import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

from .util import response, error_response
from .sendsms import send_bulk_sms, validate_body


class initiateSendBulkSms(APIView):
    def post(self, request, *args ,**kwargs):
        # message_body = request.data['body']
        # numbers = request.data['phones']
        body = request.data
        status, missing_field = validate_body(body, ['message', 'phones'])
        if not status:
            return error_response(f'{missing_field} is missing')
        send_bulk_sms(body['phones'], body['message'])
        return response(True, 'Success', None)

# {
# "message":"messageParts of the application are not loading. We're working to resolve the issue",
# "phones":["+254799143482", "+254745320466"]
# }



