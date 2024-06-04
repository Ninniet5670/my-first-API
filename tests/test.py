import json 

with open('sales.json', 'r+') as arquivo:
    sales = json.load(arquivo)

print(sales)