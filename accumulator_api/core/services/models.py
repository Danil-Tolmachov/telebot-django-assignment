from django.db import models
from core.services.abstractions import AbstractAccumulation


class AccumulationModel(models.Model):
    chat_id = models.IntegerField()

    price = models.IntegerField()
    type = models.CharField(max_length=255, null=True)
    creation_date = models.DateTimeField()
    description = models.CharField(max_length=255, null=True)

    account_id = models.CharField(max_length=255, null=True)
