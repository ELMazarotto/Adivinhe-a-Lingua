import jogos, time
from Models import session, Usuario

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
        self.name = new_user.nome

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

    def rodar(self):
        new = input("Você é um usuario [NOVO]? (s/n)")
        if new == "n":
            self.logar(input("Digite seu nome de usuário: "), input("Digite sua senha: "))
        
        else:
            self.cadastrar(input("Digite seu [NOME]: "), input("Crie uma [SENHA]: "))
        
        while True:
            print(f"Bem-Vindo {self.usuario.nome} ao LingoGuesser™.\nEsse programa tem um conceito simples...")
            btwn(2.5)
            print("Em um modo você recebe uma palavra \ne você retorna em que lingua está esta palavra.")
            wait()
            print("No outro, você tembém recebe uma palavra\nmas você retorna seu significado...")
            wait()
            skip(1)
            print("Começando...")
            wait(3)
            print("ESCOLHA UM MODO: ")
            mode = int(input("Adivinhe a Lingua(1) || Adivinhe a Tradução(2) || ENCERRAR(0): "))

            if mode == 1:
                print("MODO SELECIONADO: Adivinhe a Lingua")
                modo = int(input("MODO DIARIO(1) || MODO 100(2)"))

                if modo == 1:
                    novo_jogo = jogos.Advinhar_Lingua(jogos.palavra_aleatoria(session), 20, 5, True)

                elif modo == 2:
                    novo_jogo = jogos.Advinhar_Lingua(jogos.palavra_aleatoria(session), 400, 100, False)

                else:
                    raise ValueError("VALOR INVÁLIDO")

                novo_jogo.mostrar_palavra()
                novo_jogo.advinhar(input("Qual língua você acha que está essa palavra?"), session, self.usuario)
            
            elif mode == 2:
                print("MODO SELECIONADO: Adivinhe a Tradução")
                modo = int(input("MODO DIARIO(1) || MODO 100(2)"))

                novo_jogo = jogos.Advinhar_Traducao(jogos.palavra_aleatoria(session), 50)
                novo_jogo.mostrar_palavra()
                novo_jogo.advinhar(input("Qual o significado desta palavra?"), session, self.usuario)

            elif mode == 0:
                print("Até mais")
                break
            

            pass

programa = Programa()

programa.rodar()