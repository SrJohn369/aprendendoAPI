from sqlalchemy.orm import Session
from app.src.schema import schemas
from app.src.models import models


class RepositorioProduto:
    def __init__(self, db: Session):
        self.db = db

    def criar(self, produto: schemas.Produto):
        # trnsforma o schema json/classe para um modelo sql para salvar no db
        db_produto = models.Produto(nome=produto.nome, detalhes=produto.detalhes,
                                    preco=produto.preco, disponivel=produto.disponivel)
        self.db.add(db_produto)  # adiciona no banco
        self.db.commit()    # valida
        self.db.refresh(db_produto)     # atualiza para retornar
        return db_produto

    def listar(self):
        produtos = self.db.query(models.Produto).all()
        return produtos

    def obter(self):
        pass

    def remover(self):
        pass

