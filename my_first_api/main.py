from fastapi import FastAPI, HTTPException
from my_first_api.schemas import Sale
import json

description = """
Welcome to my-first-API tutorial!
"""

tags_metadata = [
    {
        "name": "root",
        "description": "Home route of the project",
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
        "description": "Update a sale object to the CRUD.",
    },
    {
        "name": "delete sale",
        "description": "Delete a sale object to the CRUD.",
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

with open('database/sales.json', 'r+') as arquivo:
    sales = json.load(arquivo)["items"]


@app.get('/', tags=["root"])
def root():
    return {'response': 'Hello, World! You may go to /docs ou /redoc to see further routes and test them'}

@app.get('/sale/{sale_id}', tags=["view sale"])
def view_sale(sale_id: str):
    return sales[sale_id]

@app.get('/sales', tags=["view all sales"])
def view_all_sales():
    return sales

@app.post('/sasalele/', tags=["sasalele"])
def another_view_sale(sale_info: Sale):
    return {'response': f'You just bought {sale_info.quantity} {sale_info.item} for a full R${sale_info.unit_price}? Anyways heres your id: {sale_info.id}'}

@app.post('/create_sale/', tags=["create sale"])
def create_sale(sale_info: Sale):
    sales.append(sale_info)
    return sale_info

@app.put('/update_sale/{sale_id}', tags=["update sale"])
def update_sale(sale_id:int, sale_info: Sale):
    for i, j in enumerate(sales):
        if j['id'] == sale_id:
            sales[i] = sale_info
            break
    else:
        raise HTTPException(status_code=404, detail='Not any sales with given ID')
    
    return {"response": f'Sale ID: {sale_id} updated successfully'}

@app.delete('/delete_sale/{sale_id}', tags=["delete sale"])
def delete_sale(sale_id:int):
    for i, j in enumerate(sales):
        if j['id'] == sale_id:
            del sales[i]
            break
    else:
        raise HTTPException(status_code=404, detail='Not any sales with given ID')

    return {"response": f'Sale ID: {sale_id} deleted successfully'}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('my_first_api.main:app', log_level='info', reload=True)
