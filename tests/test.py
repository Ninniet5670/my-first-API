import json 

with open('sales.json', 'wr') as arquivo:
    sales = json.load(arquivo)

print(sales)