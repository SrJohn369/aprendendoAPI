from pydantic import BaseModel
from typing import Optional, List


class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str

    
class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool

    class Config:
        orm_mode = True
    

class Pedido(BaseModel):
    id: Optional[int] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrga: bool = True
    endereco: str
    observacoes: Optional[str] = "Sem observações"


if __name__ == '__main__':
    pass
