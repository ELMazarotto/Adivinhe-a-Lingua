from palavras import palavras
from datetime import datetime
import random, time

class Jogo:
    def __int__(self, palavra ,pontuacao, limite_jogadas = None, data = None):
        self.pontuacao = pontuacao
        self.palavra = palavra
        if limite_jogadas:
            self.limite_jogadas = limite_jogadas
        if data:
            self.data = data

class Jogo_diario:
    ...

class Jogo_ilimitado:
    ...

    


#    def guess(self):
#       lingua = random.choice(palavras)
#      word = random.choice(lingua)
#
#       print(f"Qual Lingua está esta palavra?: {word.value()}")
#      lng = input("-> ")
#
#       if lng == lingua.value():
#          print("")