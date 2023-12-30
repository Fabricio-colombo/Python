'''
crie um script que peça para o usuario digitar o nome de 5 bebidas favoritas dele, armazenando esses valores em uma lista.
na sequencia, exiba na tela os elementos da lista em ordem alfabetica, um por linha, usando um laço de repetição for.
'''

bebidas_favoritas = []
for _ in range(5):
    bebida = input("Digite o nome de uma bebida favorita: ")
    bebidas_favoritas.append(bebida)

print("Bebidas favoritas em ordem alfabética:")
for bebida in sorted(bebidas_favoritas):
    print(bebida)
