from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from ulid import ulid
from fastapi.middleware.cors import CORSMiddleware  # permitir request de outras origens

app = FastAPI()

list_origens = [
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=list_origens,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class Animal(BaseModel):
    id: Optional[str] = None  # parametro opcional
    nome: str
    idade: int
    sexo: str
    cor: str


banco: List[Animal] = []


@app.get('/animais')
def listar_animais():
    return banco


@app.get("/animais/{animal_id}")
def pegar_um_animal(animal_id: str):
    for animal in banco:
        if animal.id == animal_id:
            return animal
    return {"msg": "não encontrado!"}


@app.delete("/animais/{animal_id}")
def deletar_animal(animal_id: str):
    posicao = -1
    for i, animal in enumerate(banco):
        if animal.id == animal_id:
            posicao = i
            break
    if posicao != -1:
        banco.pop(posicao)
        return {"msg": "removido!"}
    else:
        return {"msg": "não encontrado!"}


@app.post("/animais")
def adicionar_animais(animal: Animal):
    animal.id = ulid()
    animal.id = animal.id[0:8]
    banco.append(animal)
    return None
