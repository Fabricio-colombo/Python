def div():
    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite outro numero: '))
    res = round(n1 / n2, 2)
    print(res)

while True:
    try:
        div()
        break
    except ZeroDivisionError:
        print('ERROR!! Não é possivel dividir por ZERO.')
        print('TENTE NOVAMENTE')
    except ValueError:
        print('Digite apenas numeros!')
        print('TENTE NOVAMENTE')