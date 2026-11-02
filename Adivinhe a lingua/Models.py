from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from jogos import Jogo as JogoModel

db = create_engine("sqlite:///banco.db")
Base = declarative_base()
Session = sessionmaker(bind=db)
session = Session()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False, unique=True)
    senha = Column(String, nullable=False)
    pontos = Column(Integer, default=0)
    acertos = Column(Integer, default=0)
    def __init__(self, nome, senha, pontos, acertos):   
     self.nome = nome
     self.senha = senha
     self.pontos = pontos
     self.acertos = acertos

class Jogo(Base):
    __tablename__ = "jogos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    palavra_id = Column(Integer, ForeignKey("palavras.id"))
    palavra = relationship("Palavra", back_populates="palavras")
    limite_jogadas = Column(Integer)
    pontuacao = Column(Integer)
    data = Column(DateTime)
    def __init__(self, jogo : JogoModel):
       self.palavra_id = jogo.palavra.id
       self.palavra = jogo.palavra
       if jogo.pontuacao:
          self.pontuacao = jogo.pontuacao
       if jogo.limite_jogadas:
          self.limite_jogadas = jogo.limite_jogadas
       if jogo.data:
          self.data = jogo.data 
    

class Palavra(Base):
    __tablename__ = "palavras"

    id = Column(Integer, primary_key=True, autoincrement=True)
    palavra = Column(String, nullable=False)
    traducao = Column(String)
    lingua_id = Column(Integer, ForeignKey("linguas.id"), nullable=False)
    lingua = relationship("Lingua", back_populates="palavras")

class Lingua(Base):
    __tablename__ = "linguas"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    palavras = relationship("Palavra", back_populates="lingua")

Base.metadata.create_all(bind=db)
