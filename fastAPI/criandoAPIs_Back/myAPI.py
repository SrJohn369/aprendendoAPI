from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/myAPI", StaticFiles(directory="/aprendendoAPI/fastAPI/paginasTest_Front/pagina_2"), name="myAPI")

@app.get("/hello")
def hello():
    return {"message": "Hello, world!"}

