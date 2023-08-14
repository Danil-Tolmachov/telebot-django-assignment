from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class AccumulationView(APIView):
    renderer_classes = [JSONRenderer,]

    def get(self, request):
        pass
    
    def post(self, request):
        pass

    def delete(self, request):
        pass


@api_view(["GET"])
@renderer_classes([JSONRenderer,])
def get_statistics(request):
    pass
