#crie um programa que de um aumento de 10% no salario de um funcionario
#logica - 10% / 100 * salario

def aumento():
    salario = float(input('Digite qual é o seu salario atual: '))
    num = 10 / 100 * salario
    print(f"Parabéns pelo aumento de salario, seu salario foi para R${salario + num} reais")

while True:
    try:
        aumento()
        break
    except ValueError:
        print('Digite o salario corretamente!')
    except:
        print('Erro, digite corretamente')
    finally:
        print('FIM')