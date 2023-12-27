def soma(x, y):
    print(x + y)
    
def subtracao(x, y):
    print(x - y)
    
def multiplicacao(x, y):
    print(x * y)
    
def divisao(x, y):
    print(x / y)
    
print('CALCULADORA SIMPLES')
print('Escolha qual operação quer fazer')
print('Digite o numero 1 para soma')
print('Digite o numero 2 para subtracao')
print('Digite o numero 3 para multiplicacao')
print('Digite o numero 4 para divisao')

escolha = int(input('Digite o numero da operação: '))

x = float(input('Digite o primeiro numero para calcular: '))
y = float(input('Digite o segundo numero para calcular: '))

if escolha == 1:
    soma(x, y)
elif escolha == 2:
    subtracao(x, y)
elif escolha == 3:
    multiplicacao(x, y)
elif escolha == 4:
    divisao(x, y)
else:
    print("Você digitou incorretamente!")