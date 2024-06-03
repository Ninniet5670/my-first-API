from fastapi import FastAPI
from my_first_api.schemas import User
import json

tags_metadata = [
    {
        "name": "sale",
        "description": "Return sales prices. So _fancy_ they have their own docs.",
    },
    {
        "name": "user",
        "description": "Operations with users. The **login** logic is also here.",
    },
]

app = FastAPI(title='my-first-API', openapi_tags=tags_metadata)

with open('sales.json', 'r') as arquivo:
    sales = json.load(arquivo)


@app.get('/')
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
