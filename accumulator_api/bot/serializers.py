from rest_framework import serializers
from core.services.models import AccumulationModel


class AccumulationSerializer(serializers.Serializer):
    chat_id = serializers.IntegerField()

    price = serializers.IntegerField()
    type = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255, required=False)

    account_id = serializers.CharField(max_length=255, required=False)

    def create(self, validated_data):
        return AccumulationModel.create(validated_data)
