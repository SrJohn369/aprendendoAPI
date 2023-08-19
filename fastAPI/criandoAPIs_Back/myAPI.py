from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()
app.mount("/myAPI", StaticFiles(directory=Path(__file__).parent / "paginasTest_Front/pagina_2"), name="myAPI")

@app.get("/hello")
def hello():
    return {"message": "Hello, world!"}