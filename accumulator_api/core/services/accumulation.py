from core.services.abstractions import AbstractAccumulation
from core.services.models import AccumulationModel
from django.utils import timezone
from datetime import datetime


class Accumulation(AbstractAccumulation):

    def __init__(self, chat_id: int, type: str, price: int, description = None, count = 1) -> None:
        self.creation_date = timezone.now()
        self.chat_id = chat_id

        self.price = price
        self.count = count
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

    @property
    def count(self):
        return self._count
    
    @count.setter
    def count(self, var):
        self._count = var


    def get_price(self) -> int:
        return self.price

    def get_type(self) -> str:
        return self._type

    def save(self):
        """
            Save object to database
        """
        return AccumulationModel.objects.create(
            chat_id = self.chat_id,
            price = self.price,
            creation_date = self.creation_date,
            description = self.description,
            count = self.count,
            type = self._type,
        )


def load_object(obj_id: int) -> AbstractAccumulation:
    """
        Load a database record and convert it to a class object.

        Args:
            obj_id (int): The ID of the object to load from the database.

        Returns:
            AbstractAccumulation: An instance of a subclass of AbstractAccumulation
                                  based on the type field of the database record.
    """
    record = AccumulationModel.objects.get(obj_id)

    obj = Accumulation(
        record.chat_id, 
        record.type, 
        record.price,
        record.count,
        description=record.description
        )
    
    return obj
