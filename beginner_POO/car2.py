#criar uma classe carro que tenha em atributos apenas marca, modelo, ano, cor. 
#criar metodos de ligar, acelerar, freiar e desligar.

class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"{self.modelo} está ligado")
        else:
            print(f"{self.modelo} já está ligado")

    def acelerar(self):
        if self.ligado:
            self.velocidade += 2
            print(f"{self.modelo} acelerou para {self.velocidade} km/h")
        else:
            print(f"{self.modelo} precisa ser ligado para acelerar")

    def freiar(self):
        if self.ligado and self.velocidade > 0:
            self.velocidade -= 1
            print(f"{self.modelo} freiou para {self.velocidade} km/h")
        elif self.ligado:
            print(f"{self.modelo} está parado, não pode freiar mais")
        else:
            print(f"{self.modelo} precisa ser ligado para freiar")

meu_carro = Carro(marca='Peugeot', modelo='Hatch', ano=2024, cor='Green')
meu_carro.ligar()
meu_carro.acelerar()
meu_carro.freiar()
