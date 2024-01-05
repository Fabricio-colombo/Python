#crie um programa onde o usuario chegue até uma loja de automoveis e peça para ver todos os veiculos disponiveis
#assim que o vendedor mostrar, o usuario decide qual veiculo vai alugar.
#veiculos disponiveis (peugeot, hb20, corolla, hilux, fiesta)

def Peugeot():
    print('Você escolheu saber mais informações sobre o veículo Peugeot.')
    while True:
        try:
            escolha = input('O valor da diária do Peugeot é de R$60,00 reais. Aceita pegar o veículo? (sim/não): ')
            valor = 60
            escolha1 = escolha.upper()

            if escolha1 == 'SIM':
                dias = int(input('OK, agora me diga quantos dias vai ficar com o veículo? '))
                total = dias * valor
                print(f"Parabéns, acabou de alugar o veículo e o valor final a pagar é de R${total} reais.")
                break
            elif escolha1 == 'NÃO':
                print('Entendi, TCHAU!!')
                break
        except ValueError:
            print('ERROR! Digite corretamente')
            
def HB20():
    print('Você escolheu saber mais informações sobre o veículo HB20.')
    while True:
        try:
            escolha = input('O valor da diária do HB20 é de R$80,00 reais. Aceita pegar o veículo? (sim/não): ')
            valor = 80
            escolha1 = escolha.upper()

            if escolha1 == 'SIM':
                dias = int(input('OK, agora me diga quantos dias vai ficar com o veículo? '))
                total = dias * valor
                print(f"Parabéns, acabou de alugar o veículo e o valor final a pagar é de R${total} reais.")
                break
            elif escolha1 == 'NÃO':
                print('Entendi, TCHAU!!')
                break
        except ValueError:
            print('ERROR! Digite corretamente')
            
def Corolla():
    print('Você escolheu saber mais informações sobre o veículo Corolla.')
    while True:
        try:
            escolha = input('O valor da diária do Corolla é de R$110,00 reais. Aceita pegar o veículo? (sim/não): ')
            valor = 110
            escolha1 = escolha.upper()

            if escolha1 == 'SIM':
                dias = int(input('OK, agora me diga quantos dias vai ficar com o veículo? '))
                total = dias * valor
                print(f"Parabéns, acabou de alugar o veículo e o valor final a pagar é de R${total} reais.")
                break
            elif escolha1 == 'NÃO':
                print('Entendi, TCHAU!!')
                break
        except ValueError:
            print('ERROR! Digite corretamente')
            
def Hilux():
    print('Você escolheu saber mais informações sobre o veículo Hilux.')
    while True:
        try:
            escolha = input('O valor da diária da Hilux é de R$170,00 reais. Aceita pegar o veículo? (sim/não): ')
            valor = 170
            escolha1 = escolha.upper()

            if escolha1 == 'SIM':
                dias = int(input('OK, agora me diga quantos dias vai ficar com o veículo? '))
                total = dias * valor
                print(f"Parabéns, acabou de alugar o veículo e o valor final a pagar é de R${total} reais.")
                break
            elif escolha1 == 'NÃO':
                print('Entendi, TCHAU!!')
                break
        except ValueError:
            print('ERROR! Digite corretamente')
            
def Fiesta():
    print('Você escolheu saber mais informações sobre o veículo Fiesta.')
    while True:
        try:
            escolha = input('O valor da diária do Fiesta é de R$75,00 reais. Aceita pegar o veículo? (sim/não): ')
            valor = 75
            escolha1 = escolha.upper()

            if escolha1 == 'SIM':
                dias = int(input('OK, agora me diga quantos dias vai ficar com o veículo? '))
                total = dias * valor
                print(f"Parabéns, acabou de alugar o veículo e o valor final a pagar é de R${total} reais.")
                break
            elif escolha1 == 'NÃO':
                print('Entendi, TCHAU!!')
                break
        except ValueError:
            print('ERROR! Digite corretamente')
            
nome = input('Seja bem-vindo a loja de locação de veiuclos, me diga seu nome por gentileza: ')
print(f"Prazer {nome}, sou o Fabricio vendedor da loja e vou te apresentar os modelos disponiveis no momento \n")

carro1 = 'PEUGEOT'
carro2 = 'HB20'
carro3 = 'COROLLA'
carro4 = 'HILUX'
carro5 = 'FIESTA'

print(f" No momento temos 5 carros disponiveis, sendo eles: {carro1}, {carro2}, {carro3}, {carro4}, {carro5} \n")

while True:
    try:
        esc = input('Escolha o veiculo para ver informações: ')
        esc_f = esc.upper()
        
        if esc_f == carro1:
            Peugeot()
        elif esc_f == carro2:
            HB20()
        elif esc_f == carro3:
            Corolla()
        elif esc_f == carro4:
            Hilux()
        elif esc_f == carro5:
            Fiesta()
        break
    except ValueError:
        print('Erro de digitação')
    except:
        print('ERRO DESCONHECIDO!')