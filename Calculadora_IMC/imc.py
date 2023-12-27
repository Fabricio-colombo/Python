'''
Para calcular o IMC (Índice de Massa Corporal) de uma pessoa, você precisa saber o peso e a altura da pessoa.
O cálculo do IMC é feito pela fórmula: IMC = peso / altura².
O resultado do IMC pode ser interpretado de acordo com a tabela abaixo1234:

IMC	Classificação
Menor que 18,5	Magreza
18,5 a 24,9	Normal
25 a 29,9	Sobrepeso
30 a 34,9	Obesidade grau I
35 a 39,9	Obesidade grau II
Maior que 40	Obesidade grau III
'''
nome = input('Bem-vindo(a) ao consultorio, me diga seu nome: ')
peso = float(input('Me diga agora qual é o seu peso atual: '))
altura = float(input('Agora me diga, qual que é a sua altura atual: ' ))
casa_decimais = 1
res = round(peso / (altura**2), casa_decimais)

if res < 18.5:
    print(f"{nome}, seu IMC deu o resultado de {res}, e isto indica que você ta magro demais!")
elif res >= 18.5 and res <= 24.9:
    print(f"{nome}, o resultado do seu IMC deu {res}, indicando que você está com o peso normal!")
elif res >= 25 and res <= 29.9:
    print(f"{nome}, seu resultado de IMC deu {res}, e por isto indica que está com sobrepeso!")
elif res >= 30 and res <= 34.9:
    print(f"{nome}, seu resultado de IMC deu {res}, e por isto indica que você está com obesidade grau I")
elif res >= 35 and res <= 39.9:
    print(f"{nome}, seu resultado de IMC deu {res}, e por isto indica que você está com obesidade grau II")
else:
    print(f"{nome}, seu resultado de IMC deu {res}, estando com obesidade grau III")