from pydantic import BaseModel


class Animal(BaseModel):
    id_classe: int
    altura: float


class Coruja(Animal):
    id_animal: int
    raca: str
    nome: str

