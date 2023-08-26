from pydantic import BaseModel


class Animal(BaseModel):
    id: int
    altura: float


class Coruja(Animal):
    raca: str
    nome: str

