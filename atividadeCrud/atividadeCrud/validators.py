from datetime import datetime
from django.forms import ValidationError
from django.core.validators import BaseValidator

def data_menor_atual(data):
    data_atual = datetime.now().date()

    if (data_atual - data).days <= 0:
        raise ValidationError("A data de nascimento precisa ser anterior a data atual.")
    
def data_menor_igual_atual(data):
    data_atual = datetime.now().date()

    if (data_atual - data).days < 0:
        raise ValidationError("A data precisa ser anterior ou igual a data atual.")


class numero(BaseValidator):
    def __init__(self, field):
        self.limit_value = 1
        self.message = f"{field} precisa conter apenas números."
    
    def compare(self, value, b):
        try:
            int(value)
        except ValueError:
            return True

class EscolhaValidator(BaseValidator):
    def __init__(self, valores):
        self.limit_value = 1
        self.message = f"Deve estar entre os valores {valores}."
        self.valores = valores

    def compare(self, value, b):
        return value not in self.valores