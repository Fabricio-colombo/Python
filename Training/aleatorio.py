#crie um programa onde o usuario digite um numero aleatorio inteiro, se ele acertar o numero que foi gerado pelo random, ele ganha.

import random

num1 = int(input('Digite um valor inteiro (1 até 10):  '))

valor = random.randint(1, 10)

while num1 != valor:
    print('Errouu!! Tente novamente')
    num1 = int(input('Digite um valor inteiro (1 até 10):  '))
    if num1 == valor:
        print('Parabéns!! Ganhou')