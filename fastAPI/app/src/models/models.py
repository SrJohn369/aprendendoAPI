from sqlalchemy import Column, Integer, String, Float, Boolean
from app.src.config.database import Base


class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    detalhes = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)
