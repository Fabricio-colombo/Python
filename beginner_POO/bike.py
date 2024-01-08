class Bike:
    def __init__(self, altura, largura, rodas, banco, quadro, pedais):
        self.altura = altura
        self.largura = largura
        self.rodas = rodas
        self.banco = banco
        self.quadro = quadro
        self.pedais = pedais
        
    def andar_frente(self):
        print("A bike está andando para frente")
        
    def lado_direito(self):
        print("A bike virou para o lado direito")
    
    def lado_esquerdo(self):
        print('A bike andou para o lado esquerdo')
        
    def empinar(self):
        print('A bike tirou a roda da frente do chão e está empinando')
        
    def rl(self):
        print('A bike tirou a roda de trás do chão e deu RL')
        
    def parar(self):
        print('A bike parou')
        
minha_bike = Bike(altura=40, largura=110, rodas=2, banco='Couro', quadro='Metal', pedais=2)

minha_bike.andar_frente()
minha_bike.lado_direito()
minha_bike.empinar()
minha_bike.rl()
minha_bike.lado_esquerdo()
minha_bike.parar()

print(f"Minha bike tem altos banco de {minha_bike.banco}, tem de altura {minha_bike.altura} e de largura {minha_bike.largura}, é top demais")