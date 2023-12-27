def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: divisão por zero"

# Função principal da calculadora
def calculadora():
    print("Escolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite o número da operação desejada (1/2/3/4): ")

    if escolha not in ('1', '2', '3', '4'):
        print("Escolha inválida.")
        return

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print(f"{num1} + {num2} = {soma(num1, num2)}")
    elif escolha == '2':
        print(f"{num1} - {num2} = {subtracao(num1, num2)}")
    elif escolha == '3':
        print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
    elif escolha == '4':
        print(f"{num1} / {num2} = {divisao(num1, num2)}")

# Chamando a função da calculadora
calculadora()
