from fastapi import FastAPI
# Usado para servir arquivos estáticos através d API
from fastapi.staticfiles import StaticFiles
# Usando aqui para obter o camilho absoluto
from pathlib import Path

app = FastAPI()
app.mount("/myAPI", StaticFiles(directory=Path(__file__).parent / "paginasTest_Front/pagina_2"), name="myAPI")

@app.get("/hello")
def hello():
    return {"message": "Hello, world!"}