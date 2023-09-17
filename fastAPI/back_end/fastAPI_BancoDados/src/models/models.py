from pydantic import BaseModel
from typing import Optional, List


class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    minhas_vendas: List[Pedido]
    meus_pedidos: List[Pedido]
    meus_produtos: List[Produto]
    
    
class Produto(BaseModel):
    id: Optional[str] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool
    

class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrga: bool = True
    endereco: str
    observacoes: Optional[str] = "Sem observações"