from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
import uvicorn
from fastapi.templating import Jinja2Templates
from database.db import Sessionlocal
from models.orders import Order
from models.products import Product


app = FastAPI(title="Моё первое Web приложение")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    context = {
        "request": request,
        "title": "Главная страница",
        "main_text": " Здесь будет текст для главной страницы с описанием",
    }
    return templates.TemplateResponse("index.html", context=context)


@app.get("/about", response_class=HTMLResponse)
def about(request: Request):
    context = {
        "request": request,
        "title": "О нас",
        "people_count": 15,
        "mission": "Наша цель помогать людям растаться с деньгами"
    }
    return templates.TemplateResponse("about.html", context=context)


@app.get("/contacts", response_class=HTMLResponse)
def contacts(request: Request):
    context = {
        "request": request,
        "title": "Контакты",
        "adress": "ул. Павловская д.26",
        "phone": "8 (800) 555 35 35",
        "email": "top@secret.com"
    }
    return templates.TemplateResponse("contacts.html", context=context)

@app.get("/services", response_class=HTMLResponse)
def services(request: Request):
    context = {
        "request": request,
        "title": "Наши услуги",
        "service1": "Разработка веб-сайтов",
        "service2": " Дизайн интерфейсов",
        "service3": "Обслуживание серверов"
    }
    return templates.TemplateResponse("services.html", context=context)

@app.get("/orders", response_class=HTMLResponse)
def orders(request: Request):
    session = Sessionlocal()
    data = session.query(Order).all()
    session.close()

    context = {
        "request": request,
        "title": "Заказы",
        "orders": data
    }
    return templates.TemplateResponse("orders.html", context=context)

@app.get("/orders/create", response_class=HTMLResponse)
def order_create(request: Request):
    session = Sessionlocal()
    session.close()
    data =session.query(Product).all()
    context = {
        "request": request,
        "title": "Создать заказ",
        "products": data   
    }
    return templates.TemplateResponse("order_create.html", context=context)

@app.post("/orders/create", response_class=RedirectResponse)
def order_create_data(
    customer_name: str = Form(...),
    phone_nomer: str = Form(...),
    product_id: int = Form(...),
    count: int = Form(...)
):
    session = Sessionlocal()
    new_order = Order(
        customer_name=customer_name,
        phone_nomer= phone_nomer,
        product_id=product_id,
        count=count
    )
    session.add(new_order)
    session.commit()
    session.close()
    return RedirectResponse("/orders/create", status_code=303)

@app.get("/products", response_class=HTMLResponse)
def products(request: Request):
    session = Sessionlocal()
    data = session.query(Product).all()
    session.close()
    context = {
        "request": request,
        "title": "Заказы",
        "products": data
    }
    return templates.TemplateResponse("products.html", context=context)


@app.get("/product/create", response_class=HTMLResponse)
def product_create(request: Request):
    session = Sessionlocal()
    session.close()
    data =session.query(Product).all()
    context = {
        "request": request,
        "title": "Создать заказ",
        "products": data   
    }
    return templates.TemplateResponse("product_create.html", context=context)


@app.post("/product/create", response_class=RedirectResponse)
def product_create_data(
    name: str = Form(...),
    price: int = Form(...),
    count: int = Form(...)
):
    session = Sessionlocal()
    new_product = Product(
        name=name,
        price= price,
        count=count
    )
    session.add(new_product)
    session.commit()
    session.close()
    return RedirectResponse("/product/create", status_code=303)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True) 