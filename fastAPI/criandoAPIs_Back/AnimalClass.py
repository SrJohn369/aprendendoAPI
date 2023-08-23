from pydantic import BaseModel


class Animal(BaseModel):
    def __init__(self, id: int, nome: str ,altura: float):
        self.__id = id
        self.nome = nome
        self.altura = altura


class Coruja(Animal):
    def __init__(self, id: int, nome: str, raca: str, altura: float):
        super().__init__(nome, altura)
        self.__id = id
        self.raca = raca

