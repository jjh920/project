from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from app.services.product import ProductService

order_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')


@order_router.get('/order', response_class=HTMLResponse)
def order(req: Request):
    return templates.TemplateResponse('shops/order.html', {'request': req})