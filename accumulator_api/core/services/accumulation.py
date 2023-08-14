from core.services.abstractions import AbstractAccumulation
from core.services.models import AccumulationModel
from django.utils import timezone
from datetime import datetime

class BaseAccumulation(AbstractAccumulation):

    def __init__(self, chat_id: int, type: str, price: int, description = None) -> None:
        self.creation_date = timezone.now()
        self.chat_id = chat_id

        self.price = price
        self._type = type

        self.description = description
        
        super().__init__()

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, var):
        self._description = var


    @property
    def creation_date(self):
        return self._creation_date
    
    @creation_date.setter
    def creation_date(self, var):
        if isinstance(var, datetime):
            self._creation_date = var
        else:
            raise ValueError('Use "datetime" object for creation_date property')
    

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, num: int):
        self._price = num


    def get_price(self) -> int:
        return self.price

    def get_type(self) -> str:
        return self._type
    
    def save(self):
        return AccumulationModel.objects.create(
            chat_id = self.chat_id,
            price = self.price,
            creation_date = self.creation_date,
            description = self.description,
            type = self._type,
        )



class BankAccumulation(BaseAccumulation):
    
    def __init__(self, chat_id: int, type: str, price: int, account_id, description=None) -> None:
        super().__init__(chat_id, type, price, description = description)
        self._account = account_id
        self._type = 'bank'

    def get_account_id(self):
        return self._account
    
    def save(self):
        return AccumulationModel.objects.create(
            chat_id = self.chat_id,
            price = self.price,
            creation_date = self.creation_date,
            description = self.description,
            type = self._type,
            account_id = self._account,
        )

    # Extendable statytics


def load_object(obj_id: int):
    obj = AccumulationModel.objects.get(obj_id)

    if obj.type == 'bank':
        BankAccumulation(
            obj.chat_id, 
            obj.type, 
            obj.price,
            obj.account_id,
            description=obj.description
            )
    # Extendable
    else:
        BaseAccumulation(
            obj.chat_id, 
            obj.type, 
            obj.price,
            description=obj.description
            )
