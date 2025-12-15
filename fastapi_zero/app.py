from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.routers import auth, todos, users
from fastapi_zero.schemas import Message

app = FastAPI(title='Minha API')

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(todos.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
async def read_root():
    return {'message': 'Olá mundo!'}


@app.get('/exercicio-html', response_class=HTMLResponse)
async def retornar_html_aula_02():
    return """
    <html>
      <head>
        <title>Exercicio HTML</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""
