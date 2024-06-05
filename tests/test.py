import json 
from pprint import pprint

with open('sales.json', 'r+') as arquivo:
    sales = json.load(arquivo)['items']

pprint(sales[0])