from abc import ABC, abstractmethod
import requests
import json


class Singletron:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
          cls.instance = super(Singletron, cls).__new__(cls)
        return cls.instance
    

class AbstractClient(ABC):
    API_URL = None
    
    @abstractmethod
    def get_accumulation_list():
        pass

    @abstractmethod
    def get_accumulation():
        pass

    @abstractmethod
    def add_new_accumulation():
        pass

    @abstractmethod
    def delete_accumulation():
        pass
    


class DefaultClient(AbstractClient, Singletron):
    API_URL = 'http://localhost:8000/'
    
    def get_accumulation_list(self, chat_id) -> dict:
        headers = {'Authorization': str(chat_id)}
        data = requests.get(self.API_URL + 'statistics/', headers=headers)

        if 200 <= data.status_code < 300:
            return json.loads(data.text)
        else:
            return None

    def get_accumulation(self, chat_id, record_id: int):
        headers = {'Authorization': str(chat_id)}
        data = requests.get(self.API_URL + f'accumulation/?record-id={record_id}', headers=headers)
        
        if 200 <= data.status_code < 300:
            return json.loads(data.text)
        else:
            return None

    def add_new_accumulation(self, chat_id, type: str, price: int, account_id = None, description = None) -> bool:
        headers = {'Authorization': str(chat_id)}
        body = {
            'chat_id': chat_id,
            'type': type,
            'price': price,
            'account_id': account_id,
            'description': description,  
        }
        data = requests.post(self.API_URL + f'accumulation/', data=body, headers=headers)
        
        if data.status_code == 201:
            return True
        else:
            return False

    def delete_accumulation(self, chat_id, record_id: int) -> bool:
        headers = {'Authorization': str(chat_id)}
        data = requests.delete(self.API_URL + f'accumulation/?record-id={record_id}', headers=headers)
        
        if data.status_code == 201:
            return True
        else:
            return False

def create_item_message(data: dict):
    pk = data.get('pk')
    type = data.get('type')
    price = data.get('price')
    account_id = data.get('account_id')
    descriprion = data.get('description')
    
    descriprion_field = f'Description: {descriprion}\n' if descriprion is not None else ''
    account_field = f'Account id: {account_id}\n' if account_id is not None else ''

    return f'Id: {pk}\nType: {type}\nPrice: {price}\n' + account_field + descriprion_field
