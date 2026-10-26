from palavras import palavras
from Models import Palavra
import random, time

class Jogo:
    def __int__(self, pontuacao):
        self.pontuacao = pontuacao
        self.palavra : Palavra = self.palavra

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