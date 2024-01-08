'''
O robô humanoide da Tesla, chamado Optimus Gen 2, foi apresentado em dezembro de 2023.
Ele tem cerca de 1,73 metros de altura, pesa 63 kg e tem câmeras nos olhos e microfones.
A cor do robô não foi divulgada pela Tesla 1. O Optimus Gen 2 é capaz de andar mais rápido, tem maior sensibilidade nas mãos e dança 1.
Ele consegue manusear ovos facilmente e tem um pescoço com dois graus de liberdade (faz movimento para cima e para baixo, e para os lados) 1.
O robô é capaz de realizar tarefas inseguras, repetitivas e chatas 1.
O preço sugerido pelo robô Optimus é de US$ 20 mil (cerca de R$ 100 mil) 1.
'''

# nome: Optimus Gen 2
# altura: 1.73 metros
# peso: 63 kg
# caracteristicas_visuais: câmeras nos olhos, microfones
# cor: (informação não divulgada pela Tesla)
# habilidades: andar mais rápido, maior sensibilidade nas mãos, dançar, manusear ovos, realizar tarefas inseguras, repetitivas e chatas
# movimentacao_pescoço: dois graus de liberdade (movimento para cima, para baixo, e para os lados)
# preco_sugerido: US$ 20 mil (cerca de R$ 100 mil)


class Robo:
    def __init__(self, nome, altura, peso, caracteristicas_visuais, cor, movimentacao_pescoco, preco_sugerido):
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.caracteristicas_visuais = caracteristicas_visuais
        self.cor = cor
        self.movimentacao_pescoco = movimentacao_pescoco
        self.preco_sugerido = preco_sugerido
        
    def ligar(self):
        print(f"O robo {self.nome} LIGOU!!")    
        
    def andar_reto(self):
        print(f"O robo {self.nome}, está andando para frente")
        
    def andar_esquerda(self):
        print(f"O robo {self.nome} virou para a esquerda")
        
    def andar_direita(self):
        print(f"O robo {self.nome} virou para a direita")
        
    def andar_tras(self):
        print(f"O robo {self.nome} está andando para trás")
        
    def desligar(self):
        print(f"O robo {self.nome} DESLIGOU")
        
meu_robo = Robo(nome='Fabricio', altura=177, peso=90, caracteristicas_visuais='Olhos Castanhos, Microfone', cor='Branco', movimentacao_pescoco='Movimenta o pescoço para cima, baixo, esquerdo e direito', preco_sugerido=100.000)
meu_robo.ligar()
meu_robo.andar_reto()
meu_robo.andar_esquerda()
meu_robo.andar_direita()
meu_robo.desligar()
print(end='\n')
meu_robo2 = Robo(nome='Jorge', altura=195, peso=105, caracteristicas_visuais='Olhos Verdes, Camera', cor='Pardo', movimentacao_pescoco='Cima, Baixo, Direita, Esquerda', preco_sugerido=40.000)

meu_robo2.ligar()
meu_robo2.andar_reto()
meu_robo2.desligar()