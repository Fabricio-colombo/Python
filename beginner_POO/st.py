class Carro:
    def __init__(self, ano, modelo, combustivel, marca, cor):
        self.ano = ano
        self.modelo = modelo
        self.combustivel = combustivel
        self.marca = marca
        self.cor = cor
        
    def ligar(self):
        self.ligado = True
        if self.ligado == True:
            print(f"{self.marca} está ligado")
        elif self.ligado == False:
            print(f"{self.marca} está desligado")
            
meu_carro = Carro(ano=2018, modelo='Sedan', combustivel='Gasolina', marca='Peugeot', cor='Preto')
meu_carro.ligar()