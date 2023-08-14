from django.contrib import admin
from core.services.models import AccumulationModel


class ModelAdmin(admin.ModelAdmin):
    list_display = ['chat_id']


admin.site.register(AccumulationModel, ModelAdmin)
