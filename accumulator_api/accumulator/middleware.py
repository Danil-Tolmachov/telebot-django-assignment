from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.http import JsonResponse


class ChatAuthMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
            Attach chat id to request.chat_id
        """
        
        if 'Authorization' not in request.headers:
            return JsonResponse('Authorization id is not provided', status=403, safe=False)
        
        chat_id = request.headers.get('Authorization')
        request.chat_id = chat_id

        response = self.get_response(request)
        return response
