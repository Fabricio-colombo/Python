#funções lambda (anônimas)
#lambda argumentos: expressao


quadrado = lambda x: x**2

for i in range(1, 6):
    print(quadrado(i))
    
'''
Uma função lambda é uma forma de criar funções anônimas, ou seja, funções sem nome.
Elas são geralmente usadas para criar funções simples em uma única linha.
A sintaxe básica de uma função lambda é: (lambda argumentos: expressao)

soma = lambda x, y: x + y
resultado = soma(3, 5)
print(resultado)  # Saída: 8

'''

