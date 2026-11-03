from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
#from jogos import Jogo as JogoModel

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
    def __init__(self, nome, senha):   
     self.nome = nome
     self.senha = senha

class Jogo(Base):
    __tablename__ = "jogos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    palavra_id = Column(Integer, ForeignKey("palavras.id"))
    palavra = relationship("Palavra", back_populates="jogos")
    limite_jogadas = Column(Integer)
    pontuacao = Column(Integer)
    data = Column(DateTime)
    def __init__(self, jogo):
        self.palavra_id = jogo.palavra.id
        self.palavra = jogo.palavra
        self.data = jogo.data 
        if jogo.pontuacao:
          self.pontuacao = jogo.pontuacao
        if jogo.limite_jogadas:
          self.limite_jogadas = jogo.limite_jogadas


class Lingua(Base):
    __tablename__ = "linguas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False, unique=True)
    palavras = relationship("Palavra", back_populates="lingua")
    def __init__(self, nome):   
        self.nome = nome

class Palavra(Base):
    __tablename__ = "palavras"

    id = Column(Integer, primary_key=True, autoincrement=True)
    palavra = Column(String, nullable=False)
    traducao = Column(String, nullable=False)
    lingua_id = Column(Integer, ForeignKey("linguas.id"), nullable=False)
    lingua = relationship("Lingua", back_populates="palavras")
    jogos = relationship("Jogo", back_populates="palavra")
    def __init__(self, palavra, traducao, lingua:Lingua):   
     self.palavra = palavra
     self.traducao = traducao
     self.lingua = lingua

Base.metadata.create_all(bind=db)
