print('TABUADA'.center(40, "-"))
tabuada = int(input('Digite um numero para ver sua Tabuada: '))

print(f"TABUADA do numero {tabuada}".center(40, "-"))

for i in range(11):
    numero = tabuada * i
    print(f"{tabuada} X {i} = {numero}".center(40))