import jogos, time
from Models import session, Usuario, Jogo
from datetime import date
from sqlalchemy import func

def skip(amount):
    if amount > 0:
        print("\n" * amount, end="")


def btwn(mult = 1):
    time.sleep(0.4 * mult)

def wait(mult = 1):
    time.sleep(1*mult)


class Programa:

    def cadastrar(self, username, password):
        new_user = Usuario(username, password)
        session.add(new_user)
        session.commit()
        self.usuario = new_user

    def logar(self, nome, senha):
        usuuario = session.query(Usuario).filter(Usuario.nome == nome).first()
        if usuuario:
            if usuuario.senha == senha:
                print("Usuário logado")
                self.usuario = usuuario
                return True
            else:
                print("Senha incorreta")
                return False
        print("Usuário inexistente")
        return False

    def stats(self):
        print(f"Status de usuario [{self.usuario}]: ")
        print(f"   -pontos: [{self.usuario.pontos}]")
        print(f"   -acertos totais: [{self.usuario.acertos}]")
        print(f"")

    def rodar(self):
        new = input("Você é um usuario [NOVO]? (s/n)")
        if new == "n":
            self.logar(input("Digite seu nome de usuário: "), input("Digite sua senha: "))
        
        else:
            self.cadastrar(input("Digite seu [NOME]: "), input("Crie uma [SENHA]: "))

        print(f"Bem-Vindo {self.usuario.nome} ao LingoGuesser™.\nEsse programa tem um conceito simples...")
        btwn(2.5)
        print("Em um modo você recebe uma palavra \ne você retorna em que lingua está esta palavra.")
        wait(2)
        print("No outro, você tembém recebe uma palavra\nmas você retorna seu significado...")
        wait()
        skip(2)
        
        while True:
            
            print("Começando...")
            wait(5)
            print("ESCOLHA UM MODO: ")
            mode = int(input("Adivinhe a Lingua(1) || Adivinhe a Tradução(2) || Mostrar seus STATUS(3) || ENCERRAR(0): "))

            if mode == 1:
                print("MODO SELECIONADO: Adivinhe a Lingua")
                modo = int(input("MODO DIARIO(1) || MODO INFINITY-LINGO(2)"))
                if modo == 1:
                    jogo : Jogo = session.query(Jogo).filter(func.date(Jogo.data) == date.today()).first()
                    if not jogo:
                        novo_jogo = jogos.Advinhar_Lingua(jogos.palavra_aleatoria(session), 20, 5, True)
                        novo_jogo.registrar_bd(session)
                    else:
                        novo_jogo = jogos.Advinhar_Lingua(jogo.palavra, jogo.pontuacao, jogo.limite_jogadas, True)
                        if self.usuario.id in jogo.usuarios:
                            raise ValueError("Você já jogou o jogo diário de hoje")
                    novo_jogo.mostrar_palavra()
                    novo_jogo.advinhar(input("Qual língua você acha que está essa palavra?"), session, self.usuario)
                    novo_jogo.registrar_usuario(session, self.usuario.id)
                    

                elif modo == 2:
                    while True:
                        jogo_atual = jogos.Advinhar_Lingua(jogos.palavra_aleatoria(session), 5, 1, False)
                        jogo_atual.mostrar_palavra()
                        if not jogo_atual.advinhar(input("Qual língua você acha que está essa palavra?"), session, self.usuario):
                            print("GAME OVER")
                            break



                else:
                    raise ValueError("VALOR INVÁLIDO")

                
            elif mode == 2:
                print("MODO SELECIONADO: Adivinhe a Tradução")
                modo = int(input("MODO DIARIO(1) || MODO INFINITY-LINGO(2)"))

                if modo == 1:
                    jogo : Jogo = session.query(Jogo).filter(Jogo.data==date.today()).first()
                    if not jogo:
                        novo_jogo = jogos.Advinhar_Traducao(jogos.palavra_aleatoria(session), 50, 5, True)
                        novo_jogo.registrar_bd(session)
                    else:
                        novo_jogo = jogos.Advinhar_Traducao(jogo.palavra, jogo.pontuacao, jogo.limite_jogadas, True)
                        if self.usuario.id in jogo.usuarios:
                            raise ValueError("Você já jogou o jogo diário de hoje")
                    novo_jogo.mostrar_palavra()
                    novo_jogo.advinhar(input("Qual o significado desta palavra?"), session, self.usuario)

                elif modo == 2:
                    while True:
                        novo_jogo = jogos.Advinhar_Traducao(jogos.palavra_aleatoria(session), 10, 1, False)
                        novo_jogo.mostrar_palavra()
                        if not novo_jogo.advinhar(input("Qual o significado desta palavra?"), session, self.usuario):
                            print("GAME OVER")
                            break



            elif mode == 3:
                self.stats()

            elif mode == 0:
                print("Até mais")
                break

            else:
                raise ValueError(f"{mode} não é uma opção valida...")
            

            pass

programa = Programa()

programa.rodar()
