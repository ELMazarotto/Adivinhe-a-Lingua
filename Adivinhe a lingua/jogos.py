from models import Palavra, Usuario, Session
from models import Jogo as JogoBD
from datetime import date
import random, time

palavra_aleatoria = lambda session: session.query(Palavra).first() 

class Jogo:
    def __init__(self, palavra : Palavra ,pontuacao, limite_jogadas = None, diario=False, data = date.today()):
        self.pontuacao = pontuacao
        self.palavra : Palavra= palavra
        self.limite_jogadas = limite_jogadas
        if limite_jogadas:
            self.tenativas = 0
        self.diario = diario
        if diario:
            self.data = data
    def pontuar(self, usuario : Usuario, session: Session):
        usuario.acertos += 1
        if self.diario:
            if self.data == date.today():
                usuario.pontos += self.pontuacao
        session.commit()
    def advinhar(self, tentativa : str, session : Session, usuario: Usuario):
            if tentativa.lower() == self.resposta:
                print("Você acertou!")
                if self.pontuacao:
                    print("Você ganhou",self.pontuacao,"pontos!")
                    self.pontuar(usuario, session)
            else: print("Errou!")
            if self.limite_jogadas:
                self.tenativas += 1
    def registrar_bd(self, session: Session):
        novo_jogo : JogoBD = JogoBD(self)
        session.add(novo_jogo)
        session.commit()


class Advinhar_Lingua(Jogo):
    def __init__(self, palavra : Palavra ,pontuacao, limite_jogadas = None, diario = False):
        super().__init__(palavra ,pontuacao, limite_jogadas, diario)
        self.resposta = self.palavra.lingua.nome
    def mostrar_palavra(self):
        print(self.palavra.palavra)






#    def guess(self):
#       lingua = random.choice(palavras)
#      word = random.choice(lingua)
#
#       print(f"Qual Lingua está esta palavra?: {word.value()}")
#      lng = input("-> ")
#
#       if lng == lingua.value():
#          print("")