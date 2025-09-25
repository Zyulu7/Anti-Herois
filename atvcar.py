class Carro:
    def __init__(self, marca, modelo, ano, cor, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor
        print(f"{self.modelo} acelerou!")
    
    def frear(self, valor):
        self.velocidade -= valor
        print(f"{self.modelo} freou!")

    