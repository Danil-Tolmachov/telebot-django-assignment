from abc import ABC, abstractmethod


class AbstractAccumulation(ABC):
    """
        Abstraction of accumulation item
    """

    @property
    @abstractmethod
    def description(self):
        pass

    @property
    @abstractmethod
    def creation_date(self):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @property
    @abstractmethod
    def count(self):
        pass


    @abstractmethod
    def save():
        pass

    @abstractmethod
    def get_price(self) -> int:
        pass
