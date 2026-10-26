from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Word_List(db.Model):
    ...

class jogo:

    def logar(self, user, senha):
        usuario = ...
        if not usuario:
            raise Exception("Usuario não encontrado")
        if senha == usuario.senha:
            return True
        raise Exception("Senha Incorreta")