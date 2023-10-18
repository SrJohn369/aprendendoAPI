from fastapi import FastAPI, Depends
from schema.schemas import Produto
from sqlalchemy.orm import Session
from app.src.config.database import criar_db, get_db
from app.src.repositorio.produto import RepositorioProduto


criar_db()


app = FastAPI()


@app.get("/produtos")
def listar_produtos():
    pass


@app.post("/produtos")
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado
