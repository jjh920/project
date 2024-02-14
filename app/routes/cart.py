from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

cart_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')


@cart_router.get('/cart', response_class=HTMLResponse)
def cart(req: Request):
    return templates.TemplateResponse('shops/cart.html', {'request': req})


# 임시 : 카테고리 추가
@cart_router.get('/cate_write', response_class=HTMLResponse)
def cart(req: Request):
    return templates.TemplateResponse('shops/cart_write.html', {'request': req})
