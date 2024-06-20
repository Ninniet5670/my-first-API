import json 
from pprint import pprint
from my_first_api.schemas import Sale

tirar = 2

with open('database/sales.json', 'r+') as arquivo:
    sales = json.load(arquivo)['items']

# new potential mode for retrieving information
pprint(Sale.model_validate(sales[tirar]))