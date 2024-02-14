from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

shop_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')


@shop_router.get('/cart', response_class=HTMLResponse)
def cart(req: Request):
    return templates.TemplateResponse('shops/cart.html', {'request': req})


@shop_router.get('/product', response_class=HTMLResponse)
def product(req: Request):
    return templates.TemplateResponse('shops/view.html', {'request': req})


@shop_router.get('/product_detail', response_class=HTMLResponse)
def product_detail(req: Request):
    return templates.TemplateResponse('shops/product_detail.html', {'request': req})
