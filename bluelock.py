class Jogador:
    def __init__(self, nome, arma, time):
        self.nome = nome
        self.arma = arma
        self.time = time
        
    def exec(self):
        print("Randola fod")

class Forward(Jogador):
    def exec(self):
        print(f"Eu sou {self.nome}, sou um atacante, minha arma é {self.arma} e eu jogo no {self.time}.")


jog1 = Forward("Yoichi Isagi", "Chute Direto e Metavisão", "Bastard München")
jog2 = Forward("Michael Kaiser", "Kaiser Impact e Metavisão", "Re Al")

jog1.exec()
jog2.exec()