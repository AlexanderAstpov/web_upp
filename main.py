from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn


app = FastAPI(title="Моё первое Web приложение")

@app.get("/")
def home():
    return "Hello World"


@app.get("/hello")
def html_hello():
    html = """
    <html>
        <head>
        <title>Моё первое Web приложение</title>
        </head>
        <body>
            <h1>Hello World</h1>
            <p>Наша первая страница</p>
            <a href="http://localhost:8000/file">На страницу File</a>
            <br>
            <a href="http://localhost:8000/test">На страницу Test</a>
           
        </body>
    </html>
    """
    return HTMLResponse(content=html)

@app.get("/file")
def from_file():
    with open("templates/index.html", "r", encoding="utf-8") as fl:
        content = fl.read()
    return HTMLResponse(content=content) 


@app.get("/test")
def from_file():
    with open("templates/test.html", "r", encoding="utf-8") as fl:
        content = fl.read()
    return HTMLResponse(content=content) 



if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True) #reload=True сервет автоматически перезагружается при изменении кода, при рабочем варианте - убираем.