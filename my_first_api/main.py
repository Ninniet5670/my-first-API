from fastapi import FastAPI
from my_first_api.schemas import User
import uvicorn

app = FastAPI(title='my-first-API')

@app.get('/')
def root():
    return 'Hello, World! You may go to /docs to see further routes and test them'

@app.post('/user')
def user_page(user_info: User):
    return f'Hello, {user_info.username}, born in {user_info.birthday}'


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('my_first_api.main:app', log_level='info', reload=True)
