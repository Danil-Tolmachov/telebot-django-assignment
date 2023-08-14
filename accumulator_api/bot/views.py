from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from bot.serializers import AccumulationSerializer
from core.services.accumulation import load_object, Accumulation
from core.services.models import AccumulationModel


class AccumulationView(APIView):
    
    renderer_classes = [JSONRenderer,]

    def get(self, request):
        record_id = request.query_params.get('record-id')

        try:
            obj = AccumulationModel.objects.get(pk=record_id)
        except:
            return Response(status=404)
        
        if str(request.chat_id) != str(obj.chat_id):
            return Response(status=403)
        
        serializer = AccumulationSerializer(obj)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = AccumulationSerializer(data=request.data)

        if serializer.is_valid() == False:
            return Response(data="Invalid data",status=400)

        data = serializer.validated_data
        
        Accumulation(
            data.get('chat_id'),
            data.get('type'),
            data.get('price'),
            count = data.get('count'), 
            description = data.get('description'),
        ).save()

        return Response(status=201)

    def delete(self, request):
        record_id = request.query_params.get('record-id')
        
        try:
            obj = AccumulationModel.objects.get(pk=record_id)
        except:
            return Response(status=404)
        
        if str(request.chat_id) != str(obj.chat_id):
            return Response(status=403)
        
        obj.delete()
        return Response(status=201)


@api_view(["GET"])
@renderer_classes([JSONRenderer,])
def get_statistics(request):
    queryset = AccumulationModel.objects.filter(chat_id=request.chat_id)
    serializer = AccumulationSerializer(queryset, many=True)
    return Response(serializer.data)
