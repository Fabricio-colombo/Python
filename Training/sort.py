import random
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

aluno1 = input('Digite seu nome aluno: ')
aluno2 = input('Digite seu nome aluno: ')
aluno3 = input('Digite seu nome aluno: ')
aluno4 = input('Digite seu nome aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(lista)

print("A lista sorteada sera", lista)