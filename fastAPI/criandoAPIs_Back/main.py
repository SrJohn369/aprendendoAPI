# FastAPI será usada para criar nossa API
# HTTPException será usada para nos retornar uma excessão/erro no request e response
from fastapi import FastAPI, HTTPException
# StaticFiles permite servir arquivos estáticos, como imagens, arquivos CSS, arquivos JavaScript, etc., através do FastAPI.
from fastapi.staticfiles import StaticFiles
# CORSMiddleware  Essa classe é um middleware que lida com as configurações de CORS para o seu aplicativo 
# FastAPI. O CORS é uma consideração importante quando você tem um front-end (geralmente em um domínio) que 
# faz solicitações para um back-end (potencialmente em um domínio diferente).
from fastapi.middleware.cors import CORSMiddleware
# Explicação desta importação está no README
from pydantic import BaseModel


app = FastAPI()

# Configurar as origens permitidas, Caso o request venha de dominios diferentes
origins = [
    "http://127.0.0.1:5500",  # Coloque aqui a URL do seu front-end
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

proximo_id = 3

class Animal(BaseModel):
    id:int | None = None
    nome: str
    nasc: int
    cor: str

animal1 = Animal(id = 1, nome='canela', nasc=2017, cor='Caramelo')
animal2 = Animal(id = 2, nome='grogu', nasc=1973, cor='Verde')

animais = [animal1, animal2]

def buscar_animal_por_id(id: int):
    for animal in animais:
        if animal.id == id:
            return animal
    return None

@app.get('/hello')
def hello():
    return "Olá seja bem-vindo!"

@app.get('/animais')
def animais_():
    return animais

@app.get('/animais/{id}')
def obter_um_animal(id: int):
    animal = buscar_animal_por_id(id)

    if animal == None:
        raise HTTPException(
            status_code=404,
            detail="Erro 404!, Animal não encontrado!"
        )
    
    return animal

@app.delete('/animais/{id}', status_code=204)
def remover_um_animal(id: int):
    animal = buscar_animal_por_id(id)
    
    if not animal:
        raise HTTPException(
            status_code=404,
            detail= "Error 404!, Animal não encontrado!"                
        )
    
    #remover animal
    animais.remove(animal)

@app.post('/animais', status_code=201)
def novo_animal(animal: Animal):
    global proximo_id
    animal.id = proximo_id
    proximo_id += 1
    animais.append(animal)
    return None

