#faça um programa que informa se a pessoa pode votar ou não pode votar com base em sua idade.
#abaixo de 15 anos não vota. acima de 16 até 18 é opcional. acima de 18 é obrigatorio. acima de 70 anos é opcional.

nome = input('Qual é o seu nome eleitor? ')
idade = int(input('Qual é a sua idade? '))

if idade <= 15:
    print(f"{nome}, você não tem idade suficiente para votar nesta eleição.")
elif idade >= 16 and idade <=18 or idade >=70:
    print(f"{nome}, na sua idade, o voto é opcional.")
elif idade >=18 and idade <=69:
    print(f"{nome}, seu voto é obrigatorio.")