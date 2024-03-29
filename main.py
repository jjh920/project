from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.dbfactory import db_startup
from app.routes.board import board_router
from app.routes.member import member_router

app = FastAPI()

# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
app.mount('/static', StaticFiles(directory='views/static'), name='static')


@app.get("/", response_class=HTMLResponse)
async def index(req: Request):
    return templates.TemplateResponse(
        'index.html', {'request': req})


if __name__ == '_main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)
