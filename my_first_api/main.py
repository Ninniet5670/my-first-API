from fastapi import FastAPI
from my_first_api.schemas import Sale
import json

description = """
Welcome to my-first-API tutorial!
"""

tags_metadata = [
    {
        "name": "root",
        "description": "Root, home route of the project",
    },
    {
        "name": "view sale",
        "description": "Return one sale information. 'So _fancy_ they have their own docs.'",
    },
    {
        "name": "view all sales",
        "description": "Return all sales prices inside the CRUD.",
    },
    {
        "name": "sasalele",
        "description": "A print with users from body parameter.",
    },
    {
        "name": "create sale",
        "description": "Add a sale object to the CRUD.",
    },
    {
        "name": "update sale",
        "description": "Add a sale object to the CRUD.",
    },
    {
        "name": "delete sale",
        "description": "Add a sale object to the CRUD.",
    },
]

app = FastAPI(
    title='my-first-API', 
    description=description,
    summary='The strong made simple tutorial to your first API!',
    contact={
        "name": "PROENÇA, Marco",
        "email": "contato.marcoproenca@gmail.com",
    },
    openapi_tags=tags_metadata)

with open('sales.json', 'r+') as arquivo:
    sales = json.load(arquivo)


@app.get('/', tags=["root"])
def root():
    return {'response': 'Hello, World! You may go to /docs ou /redoc to see further routes and test them'}

@app.get('/sale/{sale_id}', tags=["view sale"])
def view_sale(sale_id: str):
    return sales[sale_id]

@app.get('/sales', tags=["view all sales"])
def view_sales():
    return sales

@app.post('/sasalele/', tags=["sasalele"])
def another_view_sale(sale_info: Sale):
    return {'response': f'You just bought {sale_info.quantity} {sale_info.item} for a full R${sale_info.unit_price}? Anyways heres your id: {sale_info.id}'}

@app.post('/create_sale/', tags=["create sale"])
def create_sale(sale_info: Sale):
    sales.update(sale_info)
    return sale_info

@app.put('/view_sale/', tags=["update sale"])
def create_sale(sale_id:int, sale_info: Sale):
    sales[sale_id] = sale_info
    return sale_info

@app.delete('/view_sale/', tags=["delete sale"])
def create_sale(sale_info: Sale):
    sales.append(sale_info)
    return sale_info


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('my_first_api.main:app', log_level='info', reload=True)
