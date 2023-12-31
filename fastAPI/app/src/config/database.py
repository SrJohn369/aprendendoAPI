from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./blx_banco.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# EXPLICAÇÃO DE TODA ESSA ESTRUTURA AQUI ESTÁ NO SITE DO FASTAPI https://fastapi.tiangolo.com/pt/tutorial/sql-databases/
Base = declarative_base()


def criar_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == '__main__':
    pass
