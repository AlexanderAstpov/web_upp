from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import uvicorn
from fastapi.templating import Jinja2Templates


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

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True) 