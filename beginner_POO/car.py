class Carro:
    def __init__(self, ano, modelo, marca, cor, combustivel):
        self.ano = ano
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.combustivel = combustivel
        self.ligado = True
        self.velocidade = 0

    def ligar(self):
        self.ligado = True
        if self.ligado:
            print(f"{self.marca} está ligado")
        else:
            print(f"{self.marca} precisa ser ligado")

    def acelerar(self, quantidade):
        if self.ligado:
            self.velocidade += quantidade
            print(f"{self.marca} acelerou para {self.velocidade} km/h")
        else:
            print(f"{self.marca} não pode acelerar, pois está desligado")

    def desligar(self):
        self.ligado = False
        self.velocidade = 0 
        if not self.ligado:
            print(f"{self.marca} está desligado")
        else:
            print(f"{self.marca} ainda está ligado")


meu_carro = Carro(ano=2022, modelo='Hatch', marca='Fiat', cor='Preto', combustivel='Etanol')
meu_carro.ligar()
meu_carro.acelerar(20)
meu_carro.desligar()
