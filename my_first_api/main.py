from fastapi import FastAPI
from my_first_api.schemas import User
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
        "name": "sale",
        "description": "GET example with parameters. Return sales prices. So _fancy_ they have their own docs.",
    },
    {
        "name": "user",
        "description": "POST example with body. A print with users.",
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

with open('sales.json', 'r') as arquivo:
    sales = json.load(arquivo)


@app.get('/', tags=["root"])
def root():
    return {'response': 'Hello, World! You may go to /docs ou /redoc to see further routes and test them'}

@app.get('/sale/{sale_id}', tags=["sale"])
def get_sale(sale_id: str):
    return sales[sale_id]

@app.post('/user/', tags=["user"])
def user_page(user_info: User):
    return {'response': f'Hello, {user_info.username}, born in {user_info.birthday}'}


if __name__ == '__main__':
    import uvicorn

    with open('sales.json', 'w') as arquivo:
        json.dump(sales, arquivo)

    uvicorn.run('my_first_api.main:app', log_level='info', reload=True)
